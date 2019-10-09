from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.contrib.sqla.view import ModelView
from wtforms.fields.core import SelectField
from wtforms.validators import AnyOf


class UserView(ModelView):
    can_delete = False # Desabilita exclusão
    page_size = 50 # Quantidade de item por página
    can_view_details = True # Mostrar detalhe do registro
    create_modal = True # Formulário Modal para criar usuário
    edit_modal = True # Formulário Modal para editar usuário

    column_exclude_list = ['password', 'salt', 'prefix'] # Colunas removidas da table de listagem
    column_labels = {
        'name': 'Nome',
        'email': 'E-mail',
        'phone': 'Telefone',
        'mobile': 'Celular',
        'status': 'Status'
    }
    column_searchable_list = ['name', 'email'] # Campos que poderão ser utilizados para pesquisa
    column_filters = ['id'] # Campos que poderão ser utilizado em filtro

    form_excluded_columns = ['prefix', 'salt']
    form_overrides = {
        'status':SelectField
    }
    
    form_args = {
        'name': {
            'label': 'Nome',
            'validators': []
        },
        'phone': {
            'label': 'Telefone',
            'validators': []
        },
        'mobile': {
            'label': 'Celular',
            'validators': []
        },
        'password': {
            'label': 'Senha',
            'validators': []
        },
        'status': {
            'choices':[
                (1, 'Habilitado'),
                (0, 'Desabilitado')
            ]
        }
    }

    form_widget_args = {
        'name': {
            'rows': 10,
            'style': 'color: red'
        }
    }
