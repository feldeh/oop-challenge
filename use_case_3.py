import re
class Content:
    def __init__(self, original_title: str, text: str) -> None:
        self._original_title = original_title
        self._text = text
        self._updated_title = original_title
        

class Article(Content):
    def __init__(self, original_title: str, text: str) -> None:
        super().__init__(original_title, text)
        self._updated_title = original_title
        
    def __str__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
    
    def __repr__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
        
    @property
    def original_title(self) -> str:
        return self._original_title
            
    @property
    def updated_title(self) -> str:
        return self._updated_title
    
    @updated_title.setter
    def updated_title(self, value: str) -> None:
        self._updated_title = value
        
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        

    
class Ads(Content):
    def __init__(self, original_title: str, text: str) -> None:
        super().__init__(original_title, text)
        self._updated_title = original_title
        
    def __str__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
    
    def __repr__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
        
    @property
    def original_title(self) -> str:
        return self._original_title.upper()
            
    @property
    def updated_title(self) -> str:
        return self._updated_title.upper()
    
    @updated_title.setter
    def updated_title(self, value: str) -> None:
        self._updated_title = value
        
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        
class Vacancies(Content):
    def __init__(self, original_title: str, text: str) -> None:
        super().__init__(original_title, text)
        self._updated_title = original_title
        
    def __str__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
    
    def __repr__(self) -> str:
        instance_type = re.findall(r"\.(.*?)'", f"{type(self)}")[0]
        return f'content type: "{instance_type}", original title: "{self.original_title}", new title: "{self.updated_title}", text: "{self.text}"'
        
    @property
    def original_title(self) -> str:
        return self._original_title + " - apply now!"
            
    @property
    def updated_title(self) -> str:
        return self._updated_title + " - apply now!"
    
    @updated_title.setter
    def updated_title(self, value: str) -> None:
        self._updated_title = value
        
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        
        
vac = Vacancies("tt", "rr")

art = Article("test", "test1")

ads = Ads("abcd", "zwp")

array = [art, vac, ads]

print(array)
