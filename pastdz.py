from main import logger


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

@logger
def document_person(documents):
    number_doc = input("введите номер документа: ")
    for document in documents:
        if number_doc == document['number']:
            return document['name']
    return "документа нет"

@logger
def document_shelves(documents):
    num_document = input("введите номер документа: ")
    for key, value in directories.items():
        if num_document in value:
            return key
    return "документ не существует"

@logger        
def all_document():
    for document in documents:
        type = document['type']
        number = document['number']
        name = document['name']
        print(f"{type} {number} {name}")
    return "---END---"
    

@logger    
def add_document(doc, num_, f_name, shelf):
    doc = input("введите тип документа: ")
    num_ = input("введите номер документа: ")
    f_name = input("имя фамилия: ")
    shelf = input("введите номер полки: ")
    if shelf not in directories:
        return "неверная полка"
    new_doc = dict(type=doc, number=num_, name=f_name)
    documents.append(new_doc)
    directories[shelf] += [num_]
    return "док добавлен" 

    
@logger      
def main():
    print("p - выведит имя человека которому пренадлежит документ, s -выведет номер полки на которой назодится документ, l - выведет список всех документов, a - добавит документ в каталог")
    while True:
        command = input('введите команду: ')
        if command == 'p':
            print(document_person(documents))
        elif command == 's':
            print(document_shelves(documents))
        elif command == 'l':
            print(all_document())
        elif command == 'a':
            print(add_document('doc', 'num_', 'f_name', 'shelf'))
      

#main()


if __name__ == '__main__':
    main()
