# Vehicle Fleet

<div style="text-align:center"><img src="https://1.bp.blogspot.com/-RetvqN6I-wU/YKvDoCYDlHI/AAAAAAAAShc/4NkBNcvLpK8UCS14kTDx7Flx1TxhhLBCgCLcBGAsYHQ/s800/ZF-Vehiculos-Comerciales-Ligeros.jpg" width="400"/></div>

Microservicio para el control de asignaciones de vehiculos y choferes de una flota de vehiculos

## Uso

1. Hacer fork del repositorio utilizando la opción 'Use this template'.
2. Renombrar el repositorio.
3. Crear la imagen
```shell
docker build -t image:version .
```
4. Correr la imagen

Windows:
```
docker run --rm -it --env-file=.env -v ${PWD}:/usr/src/app -p 5000:5000 --name fleet_container image:version
```
*NIX:
```
docker run --rm -it --env-file=.env -v $(pwd):/usr/src/app -p 5000:5000 --name fleet_container image:version
```

## Licencia

2022
