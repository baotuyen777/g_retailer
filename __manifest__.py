{
    'name': 'Retailer',
    'description': 'Module tuyến 2',
    'author': 'ERP3C Team',
    'depends': ['base', 'product'],
    'application': True,
    'data': [
        'security/manager_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/agency.xml',
        'views/order.xml',
        'views/policy.xml',
        'views/product_lot.xml',
        'views/sale_program.xml',
        'views/product_cat.xml',
        'views/product.xml',
        'views/users.xml',
    ],
    'application': True
}
