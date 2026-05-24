class ExceptionProxy(Exception):
    
    def __init__(self, exc , func_name):
        super().__init__(str(exc))
        self._exc = exc
        self.funcname = func_name
    
    @property
    def msg(self):
        er_msg = str(self._exc)
        return er_msg
    
    @property    
    def function(self):
        return self.funcname


def transform_exceptions(func_ls):
    result = []
    for i in func_ls:
        try: 
            i()
            result.append(ExceptionProxy("ok!" , i))
        except Exception as e:
            result.append(ExceptionProxy(e , i))
    
    return result
        
