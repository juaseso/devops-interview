# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.customer import Customer  # noqa
from app.models.order import Order  # noqa
from app.models.product import Product  # noqa
