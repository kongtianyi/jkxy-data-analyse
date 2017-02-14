# -*- code: utf-8 -*-

import pymongo


class MongoDBCleaner:
    '''
    对MongoDB中存储的数据进行数据清洗
    '''
    def __init__(self, db, collection, host="127.0.0.1", port=27017):
        self.client = pymongo.MongoClient(host=host, port=port)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def set_db(self, db):
        self.db = self.client[db]

    def set_collection(self, collection):
        self.collection = self.db[collection]

    def str_to_int(self, field, name=None):
        '''
        把某个field的数据从str类型转化为int型
        '''
        success_count = 0
        failed_count = 0
        item = self.collection.find_one()
        while type(item[field]) == str:
            id = item.pop("_id")
            try:
                item[field] = int(item[field])
                success_count += 1
            except:
                failed_count += 1
                with open("error.log", "a") as f:
                    f.write("_id: %s string to int error!\n")
                continue
            self.collection.delete_one({'_id': id})
            self.collection.insert(item)
            if name is None:
                print("One item clean finished!")
            else:
                print("%s clean finished!" % item[name])
            item = self.collection.find_one()
        print("A total of %d pieces of data were cleaned!" % (success_count+failed_count))
        print("%d successful, %d failed." % (success_count, failed_count))


if __name__ == "__main__":
    fresh = MongoDBCleaner("spider", "jkxy")
    fresh.str_to_int("course_num", "course_name")
