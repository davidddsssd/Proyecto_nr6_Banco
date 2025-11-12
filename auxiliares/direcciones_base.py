# auxiliares/direcciones_base.py
"""
Base de datos local de regiones y comunas de Chile.
Organizada por región para facilitar la selección de dirección
en el registro de clientes.
"""

# Diccionario principal: Región → Lista de Comunas
REGIONES_Y_COMUNAS = {
    "XV Región de Arica y Parinacota": [
        "Arica", "Camarones", "Putre", "General Lagos"
    ],
    "I Región de Tarapacá": [
        "Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña",
        "Colchane", "Huara", "Pica"
    ],
    "II Región de Antofagasta": [
        "Antofagasta", "Mejillones", "Sierra Gorda", "Taltal",
        "Calama", "Ollagüe", "San Pedro de Atacama",
        "Tocopilla", "María Elena"
    ],
    "III Región de Atacama": [
        "Copiapó", "Caldera", "Tierra Amarilla", "Chañaral",
        "Diego de Almagro", "Vallenar", "Alto del Carmen",
        "Freirina", "Huasco"
    ],
    "IV Región de Coquimbo": [
        "La Serena", "Coquimbo", "Andacollo", "La Higuera",
        "Paiguano", "Vicuña", "Ovalle", "Combarbalá",
        "Monte Patria", "Punitaqui", "Río Hurtado",
        "Illapel", "Canela", "Los Vilos", "Salamanca"
    ],
    "V Región de Valparaíso": [
        "Valparaíso", "Viña del Mar", "Concón", "Quintero", "Puchuncaví",
        "Casablanca", "Juan Fernández", "Isla de Pascua", "San Antonio",
        "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo",
        "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Los Andes",
        "Calle Larga", "Rinconada", "San Esteban", "San Felipe", "Llaillay",
        "Panquehue", "Putaendo", "Santa María", "Catemu", "Quillota",
        "La Calera", "Hijuelas", "La Cruz", "Nogales", "Quilpué",
        "Villa Alemana", "Limache", "Olmué"
    ],
    "RM Región Metropolitana de Santiago": [
        "Santiago", "Cerrillos", "Cerro Navia", "Conchalí", "El Bosque",
        "Estación Central", "Huechuraba", "Independencia", "La Cisterna",
        "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes",
        "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa",
        "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel",
        "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín",
        "San Miguel", "San Ramón", "Vitacura", "Colina", "Lampa", "Tiltil",
        "Puente Alto", "Pirque", "San José de Maipo", "San Bernardo", "Buin",
        "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví",
        "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo",
        "Padre Hurtado", "Peñaflor"
    ],
    "VI Región del Libertador General Bernardo O'Higgins": [
        "Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue",
        "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal",
        "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo",
        "Requínoa", "San Vicente de Tagua Tagua", "San Fernando", "Chépica",
        "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo",
        "Placilla", "Pumanque", "Santa Cruz", "Pichilemu", "La Estrella",
        "Litueche", "Marchihue", "Navidad", "Paredones"
    ],
    "VII Región del Maule": [
        "Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco",
        "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Curicó",
        "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia",
        "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral",
        "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas", "Cauquenes",
        "Chanco", "Pelluhue"
    ],
    "XVI Región de Ñuble": [
        "Chillán", "Bulnes", "Chillán Viejo", "El Carmen", "Pemuco", "Pinto",
        "Quillón", "San Ignacio", "Yungay", "Quirihue", "Cobquecura", "Coelemu",
        "Ninhue", "Portezuelo", "Ránquil", "Treguaco", "San Carlos", "Coihueco",
        "Ñiquén", "San Fabián", "San Nicolás"
    ],
    "VIII Región del Biobío": [
        "Concepción", "Coronel", "Chiguayante", "Florida", "Hualpén", "Hualqui",
        "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano",
        "Tomé", "Los Ángeles", "Alto Biobío", "Antuco", "Cabrero", "Laja",
        "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo",
        "Santa Bárbara", "Tucapel", "Yumbel", "Lebu", "Arauco", "Cañete",
        "Contulmo", "Curanilahue", "Los Álamos", "Tirúa"
    ],
    "IX Región de La Araucanía": [
        "Temuco", "Carahue", "Cholchol", "Cunco", "Curarrehue", "Freire",
        "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial",
        "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra",
        "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Angol", "Collipulli",
        "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén",
        "Renaico", "Traiguén", "Victoria"
    ],
    "XIV Región de Los Ríos": [
        "Valdivia", "Corral", "Lanco", "Máfil", "Mariquina", "Paillaco",
        "Panguipulli", "Los Lagos", "La Unión", "Futrono", "Lago Ranco",
        "Río Bueno"
    ],
    "X Región de Los Lagos": [
        "Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Llanquihue",
        "Los Muermos", "Maullín", "Puerto Varas", "Osorno", "San Juan de la Costa",
        "San Pablo", "Puyehue", "Purranque", "Río Negro", "Castro", "Ancud",
        "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén",
        "Quellón", "Quemchi", "Quinchao", "Chaitén", "Futaleufú", "Hualaihué",
        "Palena"
    ],
    "XI Región de Aysén del General Carlos Ibáñez del Campo": [
        "Coyhaique", "Lago Verde", "Aysén", "Cisnes", "Guaitecas",
        "Chile Chico", "Río Ibáñez", "Cochrane", "O'Higgins", "Tortel"
    ],
    "XII Región de Magallanes y de la Antártica Chilena": [
        "Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Porvenir",
        "Primavera", "Timaukel", "Natales", "Torres del Paine", "Cabo de Hornos",
        "Antártica"
    ]
}

# --- Funciones auxiliares ---

def listar_regiones():
    """Devuelve una lista con los nombres de todas las regiones."""
    return list(REGIONES_Y_COMUNAS.keys())

def listar_comunas_por_region(region: str):
    """Devuelve la lista de comunas de una región específica."""
    return REGIONES_Y_COMUNAS.get(region, [])

def obtener_comuna(region: str, indice: int):
    """Devuelve una comuna por índice dentro de una región."""
    comunas = listar_comunas_por_region(region)
    if 1 <= indice <= len(comunas):
        return comunas[indice - 1]
    return None