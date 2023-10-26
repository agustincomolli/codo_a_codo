#!/bin/bash

# Verifica si se proporcionó un parámetro
if [ $# -eq 0 ]; then
  echo "Uso: $0 <start|stop>"
  exit 1
fi

# Verifica si el parámetro es "start"
if [ "$1" == "start" ]; then
  # Inicia MySQL
  echo "Iniciando MySQL..."
  net start MySQL80
  echo "MySQL ha sido iniciado."

# Verifica si el parámetro es "stop"
elif [ "$1" == "stop" ]; then
  # Detiene MySQL
  echo "Deteniendo MySQL..."
  net stop MySQL80
  echo "MySQL ha sido detenido."

else
  # Si el parámetro no es válido
  echo "Uso: $0 <start|stop>"
  exit 1
fi

exit 0

