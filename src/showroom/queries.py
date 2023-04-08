from src.core.repositories import ModelRepositories 

class ShopRepositories(ModelRepositories):
    def __init__(self, model_type):
        super().__init__(model_type)

    def shop_by_category_id(self,category_id):        
        the_ob = self._session.query(self._model_type).filter_by(shop_categories=category_id,is_active=True).all()
        return the_ob
