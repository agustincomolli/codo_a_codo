from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Esto permite a todas las rutas aceptar solicitudes de origen cruzado. Para
# producción, deberías limitar esto a orígenes conocidos.
CORS(app)


def get_database_uri():
    """
    Construye y retorna la URI para la conexión con la base de datos MySQL.
    """
    user = 'root'
    password = 'eggh-22cgFb-gBg4aH6DfFAC14edeFC6'
    db_name = 'railway'
    host = 'viaduct.proxy.rlwy.net'
    port = 51991
    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


# Configuración de la URI de la base de datos obtenida desde la función get_database_uri
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
# Desactivar el seguimiento de las modificaciones para evitar gasto extra de memoria
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la extensión de SQLAlchemy con la aplicación Flask
db = SQLAlchemy(app)


class ProductModel(db.Model):
    """
    Define la estructura de la tabla 'product' utilizando SQLAlchemy ORM.
    """
    __tablename__ = 'product'
    # Identificador único para cada producto
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)  # Nombre del producto
    description = db.Column(db.String(120))  # Descripción del producto


# Crear las tablas en la base de datos basándose en los modelos definidos
with app.app_context():
    db.create_all()


@app.route('/products', methods=['POST'])
def create_product():
    """
    Crea un nuevo producto en la base de datos basado en los datos JSON proporcionados.
    """
    data = request.get_json()
    product = ProductModel(name=data['name'], description=data['description'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.id), 201


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Recupera un producto por su ID y lo devuelve en formato JSON.
    """
    product = ProductModel.query.get(product_id)
    if product:
        return jsonify({'name': product.name, 'description': product.description})
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route('/products', methods=['GET'])
def get_products():
    """
    Recupera y devuelve todos los productos en la base de datos en formato JSON.
    """
    products = ProductModel.query.all()
    return jsonify([{'id': prod.id, 'name': prod.name, 'description': prod.description} for prod in products])


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Actualiza un producto existente basándose en el ID y los datos JSON proporcionados.
    """
    product = ProductModel.query.get(product_id)
    if product:
        data = request.get_json()
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        db.session.commit()
        return jsonify({'id': product.id, 'name': product.name, 'description': product.description})
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Elimina un producto de la base de datos basándose en el ID proporcionado.
    """
    product = ProductModel.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({}), 204
    else:
        return jsonify({'message': 'Product not found'}), 404


# Comprueba si el archivo es el punto de entrada principal para iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
