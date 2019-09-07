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
        print(self.listener.called_methods)

        methodName = list(self.listener.called_methods.keys())
        print("<メソッド名➀>")
        print(methodName[0])
        print("<メソッド呼び出し➀>")
        # print(self.listener.called_methods[methodName[0]][0])
        for callmethod1 in self.listener.called_methods[methodName[0]][0]:
            print(callmethod1)
        # print(len(self.listener.called_methods[methodName[0]][0]))
        print("-------------------------------------------------")
        print("<メソッド名➁>")
        print(methodName[1])
        print("<メソッド呼び出し➁>")
        for callmethod2 in self.listener.called_methods[methodName[1]][0]:
            print(callmethod2)
        # print(self.listener.called_methods[methodName[1]][0])
        # print(len(self.listener.called_methods[methodName[1]][0]))
       
        print("-------------------------------------------------")
        if len(self.listener.called_methods[methodName[0]][0]) <= len(self.listener.called_methods[methodName[1]][0]):
            num = len(self.listener.called_methods[methodName[1]][0])
            print("メソッド呼び出しの数 " + str(num))
            callmethod1 = self.listener.called_methods[methodName[1]][0]
            callmethod2 = self.listener.called_methods[methodName[0]][0]
        else:
            num = len(self.listener.called_methods[methodName[0]][0])
            print("メソッド呼び出しの数 " + str(num))
            callmethod1 = self.listener.called_methods[methodName[0]][0]
            callmethod2 = self.listener.called_methods[methodName[1]][0]

        callMethodnum = []
        for method1 in callmethod1:
            for method2 in callmethod2:
                if method1 == method2:
                    index = callmethod2.index(method2)
                    # print(index)
                    # print(method1)
                    callMethodnum.append(method1)
                    callmethod2[index] = ""
                    pass
                else:
                    pass

        print("メソッド呼び出しの差異 " + str(len(callMethodnum)) + "/" + str(num))
