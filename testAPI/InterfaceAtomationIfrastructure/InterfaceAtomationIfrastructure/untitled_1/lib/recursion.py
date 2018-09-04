class GetDictParam:

    def __init__(self):

        pass

    def get_value(self, my_dict, key):
        '''字典取值方法'''
        if isinstance(my_dict, dict):

            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if self.get_value(my_dict.get(my_dict_key), key) or \
                                self.get_value(my_dict.get(my_dict_key), key) is False:
                    return self.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if self.get_value(my_dict_arr, key) \
                        or self.get_value(my_dict_arr, key) is False:
                    return self.get_value(my_dict_arr, key)

    def list_for_key_to_dict(self, my_dict,*args):

        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: self.get_value(my_dict, key)})
        return result
