import logging.config
from ast.ast_processor import AstProcessor
from ast.basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    # target_file_path = 'C:/pbl/home/junit/src/test/java/jp/enpit/cloud/junit/CalculatorTest.java'
    target_file_path = 'C:/Users/ryosuke-ku/Desktop/callMethodDiffFile/Sample(62).java'
    # target_file_path = 'C:/Users/ryosuke-ku/Desktop/NiCad-5.1/systems/maven/maven-model-builder/src/main/java/org/apache/maven/model/interpolation/StringSearchModelInterpolator.java'

    # ★ポイント１
    ast_info = AstProcessor(None, BasicInfoListener()).execute(target_file_path)