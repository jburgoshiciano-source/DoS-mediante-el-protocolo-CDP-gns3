# DoS-mediante-el-protocolo-CDP-gns3

**Estudiante:**  Juan Francisco Burgos Hiciano

**Matrícula:**  2023-1981

**Asignatura:**  Seguridad en Redes

**Fecha:**  06 Febrero 2026

**Link del video**: [https://youtu.be/s6Emg7BInSg](https://youtu.be/DgTl9wyqAUs)


---

Descripción y Topología del Escenario

El laboratorio se implementó en GNS3 para simular una red corporativa básica vulnerable a ataques internos de Capa 2, donde un equipo Kali Linux actúa como atacante y ejecuta un DoS mediante CDP contra un switch Cisco IOU L2, saturando su tabla de vecinos. La topología incluye un router Cisco (R1) como gateway, un cliente legítimo (VPCS) y un Cloud (VMnet13) para conectividad externa, siendo el switch el objetivo principal del ataque..


### Detalles de la Topología
* **Segmentación de Red:** Se ha configurado la **VLAN 2295** (basada en los últimos 4 dígitos de la matrícula).
* **Direccionamiento IP:** Subred `198.1.98.0/24`.
* **Infraestructura:**
    * **Router Cisco c7200**
    * **Switch Cisco IOU L2**
* **Actores:**
    * **Atacante:** Kali Linux (IP `198.1.98.60`).
    * **Víctima:** PC1 / VPCS (IP `198.1.98.10.`).

<img width="888" height="650" alt="Image" src="https://github.com/user-attachments/assets/d3be5c83-f0de-4a50-a954-edcb1d3cc823" />

### Tabla de Direccionamiento

| Dispositivo | Dirección IP | Máscara de Subred | Gateway Predeterminado |
| :--- | :--- | :--- | :--- |
| **Router Gateway** | 198.1.98.1 | 255.255.255.0 (/24) | N/A |
| **Kali Linux (Atacante)** | 198.1.98.60 | 255.255.255.0 (/24) | 198.1.98.1 |
| **PC1 (Víctima)** | 198.1.98.10 | 255.255.255.0 (/24) | 198.1.98.1 |
---

 Requisitos Previos y Herramientas

Para la ejecución exitosa de estos scripts, se requiere el siguiente entorno:

* **Sistema Operativo:** Kali Linux o cualquier distribución Linux basada en Debian.
* **Lenguaje:** Python 3.x.
* **Librerías:** `Scapy` (Instalación: `sudo apt install python3-scapy`).
* **Privilegios:** Acceso **Root** (sudo) es obligatorio para la inyección de paquetes en crudo y la manipulación de interfaces de red.

---

 Ataque : DoS mediante Inundación CDP 

 ### Objetivo del Script
El script `ataque_cdp2.py` El objetivo del script es ejecutar un ataque de Denegación de Servicio (DoS) mediante el protocolo CDP, enviando paquetes CDP falsificados desde un equipo atacante para saturar la tabla de vecinos del switch Cisco, afectando su plano de control y la capacidad de administración del dispositivo dentro de un entorno de laboratorio controlado.

### Parámetros Usados
* **Interfaz:** `eth0`
* **Dirección Destino:** Multicast Cisco 
    * *Device ID:* Generado aleatoriamente 
    * *Port ID:* Simulación de interfaces Ethernet 
    * *Capabilities:* Generadas de forma aleatoria para simular distintos tipos de dispositivos de red

---

Medidas de Mitigación
Para proteger la infraestructura contra estos vectores de ataque, se recomiendan las siguientes configuraciones de endurecimiento (Hardening):

Contra CDP 
Deshabilitar CDP: En todas las interfaces que conectan a usuarios finales o zonas no confiables.
```bash
Switch(config-if)# no cdp run
```

