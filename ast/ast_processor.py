from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast.JavaLexer import JavaLexer
from ast.JavaParser import JavaParser
from pprint import pformat


class AstProcessor:

    def __init__(self, logging, listener):
        # self.logging = logging
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    def execute(self, input_source):
        parser = JavaParser(CommonTokenStream(JavaLexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        # print(self.listener.called_methods)
        # print(self.listener.methods)

        # for method in self.listener.called_methods:
        #     print("<メソッド名>")
        #     print(method)
        #     print("<メソッド呼び出し>")
        #     for callmethod in self.listener.called_methods[method][0]:
                
        #         print(callmethod)

        methodName = list(self.listener.called_methods.keys())
        print(methodName[0])
        print(methodName[1])
        print(self.listener.called_methods[methodName[0]][0])
        # print(len(self.listener.called_methods[methodName[0]][0]))
        print(methodName[1])
        print(self.listener.called_methods[methodName[1]][0])
        # print(len(self.listener.called_methods[methodName[1]][0]))
       

        if len(self.listener.called_methods[methodName[0]][0]) <= len(self.listener.called_methods[methodName[1]][0]):
            num = len(self.listener.called_methods[methodName[0]][0])
            print(num)

        j = []
        for i in range(int(num)):
            if self.listener.called_methods[methodName[0]][0][i] == self.listener.called_methods[methodName[1]][0][i]:
                j.append(1)
            else:
                j.append(0)
        # print(j)
        print(str(j.count(1)) + "/" + str(num))
        # print(j.count(1)/int(num))