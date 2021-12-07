from django import forms


modelos = [
	('0', 'No tengo vehículo'),
	('1', 'Pequeño'),
    ('2', 'Mediano'),
    ('3', 'Grande'),
    ]

dieta = [
	('0', 'Rico en carnes'),
	('1', 'Dieta promedio'),
    ('2', 'Sin carnes rojas'),
    ('3', 'Vegano'),
    ('4', 'Vegetariano'),
    ]


class ProductForm(forms.Form):

	Cantidad = forms.FloatField(label='¿Cuantas personas viven en tu casa?', min_value=1,max_value=14, required = True)
	ModelAuto = forms.FloatField(label='¿Que tipo de vehículo tienes?', widget=forms.Select(choices=modelos), required = True)
	Usos = forms.FloatField(label='¿Cuantos kilometros al día recorres en tu vehículo?', min_value=0, required=True )
	Días = forms.FloatField(label='¿Cuantos días a la semana utilizas transporte público?',min_value=0,max_value=14, required = True)
	Luz = forms.FloatField(label='¿Cuanto es tu cuenta de luz al año?', min_value=1000, required = True)
	Gas = forms.FloatField(label='¿Cuanto es tu cuenta de gas al año?', min_value=1000, required = True)
	Dieta = forms.FloatField(label='¿Que tipo de dieta tienes?', widget=forms.Select(choices=dieta), required = True)
	Plastico = forms.FloatField(label='¿Cuantos [Kg] de plástico consideras consumir al año?',min_value=1,required = True)