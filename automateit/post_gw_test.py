import requests

payload = {
'ID_PORTAL': '26',  		## en materiales
'ID_USUARIO_PORTAL': '114',   ## usuario de alexander @ cmd
'PRODUCTOS': {'ID_PRODUCTO': 109884,'CANTIDAD': 1},    ## un producto de EnMateriales
'ID_PAGO_PORTAL': '20180706',	## variable timestamp
'ID_MEDIO_PAGO': '60',
'ID_GATEWAY': '11'  		## MP
}

r = requests.post("https://bac.cmd.com.ar/backend_web/pago/crearPago.htm", data=payload)
print("Response text:", r.text)
