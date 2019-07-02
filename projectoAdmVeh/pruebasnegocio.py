from negocio.tipoVehiculo import TipoVehiculo



res = TipoVehiculo.getAllTipos(TipoVehiculo)
for i in res:
    print(i)