class Item:
    def __init__(self, name, price, category):
        if price <= 0:
            raise ValueError(f'Invalid value for price, got {price}')
            
        self._name = name
        self._price = price
        self._category = category
        
    @property
    def name(self):
        return self._name
        
    @property
    def price(self):
        return self._price
        
    @property
    def category(self):
        return self._category
        
    def __str__(self):
        return f'{self._name}@{self._price}-{self._category}'
        
class Query:
    valid_operations = ['IN', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']
    
    def __init__(self, field, operation, value):
        if operation not in self.valid_operations:
            raise ValueError(f'Invalid value for operation, got {operation}')
            
        self._field = field
        self._operation = operation
        self._value = value
        
    @property
    def field(self):
        return self._field
        
    @property
    def operation(self):
        return self._operation
    
    @property
    def value(self):
        return self._value
        
    def __str__(self):
        return f'{self._field} {self._operation} {self._value}'
        
class Store:
    def __init__(self):
        self._items_in_store = []
        
    @property
    def items_in_store(self):
        return self._items_in_store
    
    def __str__(self):
        if len(self.items_in_store)!= 0:
            return "\n".join(map(str, self.items_in_store))
        else:
            return 'No items'
    
    def add_item(self, item):
        self.items_in_store.append(item)
    
    def count(self):
        return len(self.items_in_store)
        
    def __add__(self, other):
        added_items = Store()
    
        for item in self.items_in_store:
            added_items.add_item(item)
        
        for item in other.items_in_store:
            added_items.add_item(item)
            
        return added_items
        
    def filter(self, query):
        filtered_items = Store()
        
        for item in self.items_in_store:
            value = getattr(item, query.field)
            if query.operation == "EQ" and value == query.value:
                filtered_items.add_item(item)
                
            if query.operation == "GT" and value > query.value:
                filtered_items.add_item(item)
                
            if query.operation == "GTE" and value >= query.value:
                filtered_items.add_item(item)
                
            if query.operation == "LT" and value < query.value:
                filtered_items.add_item(item)
            
            if query.operation == "LTE" and value <= query.value:
                filtered_items.add_item(item)
                
            if query.operation == "STARTS_WITH" and value.startswith(query.value):
                filtered_items.add_item(item)
                
            if query.operation == "ENDS_WITH" and value.endswith(query.value):
                filtered_items.add_item(item)
                
            if query.operation == "CONTAINS" and value.__contains__(query.value):
                filtered_items.add_item(item)
                
            if query.operation == "IN" and value in query.value:
                filtered_items.add_item(item)
        return filtered_items
        
    def exclude(self, query):
        excluded_filtered_items = Store()
        included_filtered_items = self.filter(query)
        
        for i in self.items_in_store:
            if i not in included_filtered_items.items_in_store:
                excluded_filtered_items.add_item(i)
        return excluded_filtered_items