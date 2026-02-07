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

![Topología del laboratorio](https://github.com/user-attachments/assets/d5f2953c-e147-4316-a8a8-866b22f38e8c)






















