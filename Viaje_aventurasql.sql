CREATE DATABASE IF NOT EXISTS ViajeAventuraDB;
USE ViajeAventuraDB;

CREATE TABLE Cliente (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    rut VARCHAR(20) UNIQUE,
    correo VARCHAR(100),
    contrasena VARCHAR(255),
    telefono VARCHAR(20)
);

CREATE TABLE Destino (
    idDestino INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    actividades TEXT,
    costo DECIMAL(10,2)
);

CREATE TABLE PaqueteTuristico (
    idPaquete INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    precio DECIMAL(10,2)
);

CREATE TABLE PaqueteDestino (
    Paquete_idPaquete INT,
    Destino_idDestino INT,
    PRIMARY KEY (Paquete_idPaquete, Destino_idDestino),
    FOREIGN KEY (Paquete_idPaquete) REFERENCES PaqueteTuristico(idPaquete) ON DELETE CASCADE,
    FOREIGN KEY (Destino_idDestino) REFERENCES Destino(idDestino)
);

CREATE TABLE Reserva (
    idReserva INT AUTO_INCREMENT PRIMARY KEY,
    Cliente_idCliente INT,
    Paquete_idPaquete INT,
    fecha_reserva DATE,
    estado VARCHAR(50),
    FOREIGN KEY (Cliente_idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (Paquete_idPaquete) REFERENCES PaqueteTuristico(idPaquete)
);

-- Usuario admin inicial
INSERT INTO Cliente (nombre, rut, correo, contrasena, telefono) 
VALUES ('Administrador', '12345', 'admin@viajes.com', 
        '$2b$12$... (usa Seguridad.encriptar_clave("ADMIN123"))', '999999999');