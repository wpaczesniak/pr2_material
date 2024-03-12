class Aeropuerto:
	def __init__(self):
		self.ID = 0
		self.nombre = "\\N"
		self.ciudad = "\\N"
		self.pais = "\\N"
		self.IATA = "\\N"
		self.ICAO = "\\N"
		self.latitud = 0.0
		self.longitud = 0.0
		self.altitud = 0.0
		self.timezone = 0.0
		self.DST = "\\N"

	def SetID(self, ID):
		self.ID = ID

	def GetID(self):
		return self.ID

	def SetNombre(self, nombre):
		self.nombre = nombre

	def GetNombre(self):
		return self.nombre

	def SetCiudad(self, ciudad):
		self.ciudad = ciudad

	def GetCiudad(self):
		return self.ciudad

	def SetPais(self, pais):
		self.pais = pais

	def GetPais(self):
		return self.pais

	def __ValidarIATA(self, s):
		return len(s) == 3 and s.isupper() or s == "\\N"

	def SetIATA(self, IATA):
		if self.__ValidarIATA(IATA):
			self.IATA = IATA
		else:
			raise RuntimeError("Error: IATA debe ser una secuencia de 3 letras mayúsculas o '\\N'.")

	def GetIATA(self):
		return self.IATA

	def __ValidarICAO(self, s):
		return len(s) == 4 and s.isupper() or s == "\\N"

	def SetICAO(self, ICAO):
		if self.__ValidarICAO(ICAO):
			self.ICAO = ICAO
		else:
			raise RuntimeError("Error: ICAO debe ser una secuencia de 4 letras mayúsculas o '\\N'.")

	def GetICAO(self):
		return self.ICAO

	def SetLatitud(self, latitud):
		self.latitud = latitud

	def GetLatitud(self):
		return self.latitud

	def SetLongitud(self, longitud):
		self.longitud = longitud

	def GetLongitud(self):
		return self.longitud

	def SetAltitud(self, altitud):
		self.altitud = altitud

	def GetAltitud(self):
		return self.altitud

	def SetTimezone(self, timezone):
		self.timezone = timezone

	def GetTimezone(self):
		return self.timezone

	def __ValidarDST(self, s):
		return s in {'E', 'A', 'S', 'O', 'Z', 'N', 'U', "\\N"}

	def SetDST(self, DST):
		if self.__ValidarDST(DST):
			self.DST = DST
		else:
			raise RuntimeError("Error: DST debe ser alguno de los siguientes valores: E, A, S, O, Z, N, U o '\\N'.")

	def GetDST(self):
		return self.DST

	def __str__(self):
		return f"{self.ID};{self.nombre};{self.ciudad};{self.pais};{self.IATA};{self.ICAO};" \
			   f"{self.latitud};{self.longitud};{self.altitud};{self.timezone};{self.DST}"