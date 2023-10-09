#!/bin/bash

for i in {02..29}; do
  # Crear el directorio si no existe.
  mkdir -p "./ejercicio-$i"
  cp ./ejercicio-01/* "./ejercicio-$i/"
done

