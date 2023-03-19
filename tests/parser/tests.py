from parser import parser
import hashlib
def test_empty_html():
    assert parser.Parser("https://www.blank.org/").get_text_html()=='\nblank\n.\n'

def test_empty_pdf():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\empty.pdf").get_text_pdf()=='\n'

def test_empty_docx():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\empty.docx").get_text_docx()=='\n'

def test_empty_doc():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\empty.doc").get_text_doc()==''

def test_text_pdf():
    true = '\nСупер док\nНа\nРусском'
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple.pdf").get_text_pdf()==true

def test_text_docx():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple.docx").get_text_docx()=='\nСупер док\nНа\n                                                        Русском'

def test_text_doc():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple.doc").get_text_doc()=='\nСупер док\nНа\n                                                        Русском'

def test_text_html_form():
    readFile= open(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\standart_test_form.txt",encoding='utf-8').read()
    assert hashlib.sha256(parser.Parser("https://www.lipsum.com/").get_text_html(False).encode()).hexdigest()==hashlib.sha256(readFile.encode()).hexdigest()

def test_bi_lang_html_():
    readFile = open(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\bi_lang.txt", encoding='utf-8').read()
    results = parser.Parser("https://umnazia.ru/blog/all-articles/vremena-goda-na-anglijskom").get_text_html(True).encode().decode('utf-8')
    assert hashlib.sha256(results.encode()).hexdigest()==hashlib.sha256(readFile.encode()).hexdigest()

def test_bi_lang_pdf():
    true = '\nСупер док\nНа\nРусском\nand on\nENGLICH!!!'
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple_bi.pdf").get_text_pdf()==true

def test_bi_lang_docx():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple_bi.docx").get_text_docx()=='\nСупер док\nНа\n                                                        Русском\n\nand on\n\nENGLICH!!!'

def test_bi_lang_doc():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\simple_bi.doc").get_text_doc()=='\nСупер док\nНа\n                                                        Русском\n\nand on\n\nENGLICH!!!'



def test_link_html():
    trusted = ['https://my.spbu.ru/DXR.axd?r=24_378-6qUui',
 'https://my.spbu.ru/DXR.axd?r=24_379-6qUui',
 'https://my.spbu.ru/DXR.axd?r=24_383,0_5411,0_5412,1_67,1_69-6qUui',
 'https://my.spbu.ru/DXR.axd?r=0_5418,0_5424,1_251,0_5331,0_5332,1_250-FpUui',
 'https://my.spbu.ru/DXR.axd?r=0_5338,1_73,1_74,1_72-FpUui',
 'https://edu.spbu.ru/maps/map.html ']
    links = parser.Parser("https://my.spbu.ru/Login.aspx?ReturnUrl=%2f").get_links_html()
    assert links==trusted

def test_img_html():
    trusted = ['https://my.spbu.ru/images/favicon-32x32_0.png', 'https://my.spbu.ru/DXR.axd?r=1_110-DpUui', 'https://my.spbu.ruDXX.axd?handlerName=ImageResource&name=Security_Image&enbl=True&fldr=TemplatesV2Images&v=', 'https://my.spbu.ru/DXR.axd?r=1_110-DpUui']
    links = parser.Parser("https://my.spbu.ru/Login.aspx?ReturnUrl=%2f").get_img_html()
    assert links == trusted

def test_table_pdf():
    true = [[['это', 'таблица'], ['this is', 'table']]]
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\table.pdf").get_tables_pdf(0)==true

def test_table_docx():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\table.docx").get_tables_docx_doc()==[[['это', 'таблица'], ['this is', 'table']]]

def test_table_doc():
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\table.doc").get_tables_docx_doc()==[[['это', 'таблица'], ['this is', 'table']]]

# def test_link_pdf():
#     true = [
#         'https://www.google.com/search?q=%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzWPEuuGdWeu2CDUeteSLjKiaqcj2w%3A1679255731956&ei=s2gXZJ7-OavqrgThlqCwBg&oq=&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgwIABDqAhC0AhBDGAEyDAgAEOoCELQCEEMYATIMCAAQ6gIQtAIQQxgBMg8IABDqAhC0AhBDEIsDGAEyDwgAEOoCELQCEEMQiwMYATIYCC4QyAMQ6gIQtAIQQxCLAxCcAxCoAxgCMg8ILhDIAxDqAhC0AhBDGAIyGAguEMgDEOoCELQCEEMQiwMQqAMQnAMYAkoECEEYAFAAWABgrgdoAXABeACAAQCIAQCSAQCYAQCgAQGwARK4AQHAAQHaAQYIARABGAHaAQYIAhABGAg&sclient=gws-wiz-serp',
#         'https://www.google.com/search?q=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzVWzVeABBFfgV_ucwH2kz_PqNDcDQ%3A1679256070096&ei=BmoXZJzBBYnOrgTl_bCoCw&oq=%D0%B0%D0%BD%D0%B3%D0%BB&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgQIIxAnMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMggIABCABBCxAzILCAAQgAQQsQMQgwEyBAgAEEMyBAgAEEMyBAgAEEM6BQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoECC4QQ0oECEEYAFAAWJ0DYPELaABwAXgAgAFZiAGSApIBATSYAQCgAQHAAQE&sclient=gws-wiz-serp']
#     assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\link.pdf").get_links_pdf()==true

def test_link_docx():
    true = [
        'https://www.google.com/search?q=%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzWPEuuGdWeu2CDUeteSLjKiaqcj2w%3A1679255731956&ei=s2gXZJ7-OavqrgThlqCwBg&oq=&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgwIABDqAhC0AhBDGAEyDAgAEOoCELQCEEMYATIMCAAQ6gIQtAIQQxgBMg8IABDqAhC0AhBDEIsDGAEyDwgAEOoCELQCEEMQiwMYATIYCC4QyAMQ6gIQtAIQQxCLAxCcAxCoAxgCMg8ILhDIAxDqAhC0AhBDGAIyGAguEMgDEOoCELQCEEMQiwMQqAMQnAMYAkoECEEYAFAAWABgrgdoAXABeACAAQCIAQCSAQCYAQCgAQGwARK4AQHAAQHaAQYIARABGAHaAQYIAhABGAg&sclient=gws-wiz-serp',
        'https://www.google.com/search?q=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzVWzVeABBFfgV_ucwH2kz_PqNDcDQ%3A1679256070096&ei=BmoXZJzBBYnOrgTl_bCoCw&oq=%D0%B0%D0%BD%D0%B3%D0%BB&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgQIIxAnMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMggIABCABBCxAzILCAAQgAQQsQMQgwEyBAgAEEMyBAgAEEMyBAgAEEM6BQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoECC4QQ0oECEEYAFAAWJ0DYPELaABwAXgAgAFZiAGSApIBATSYAQCgAQHAAQE&sclient=gws-wiz-serp']
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\link.docx").get_links_docx() == true
def test_link_doc():
    true = [
        'https://www.google.com/search?q=%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzWPEuuGdWeu2CDUeteSLjKiaqcj2w%3A1679255731956&ei=s2gXZJ7-OavqrgThlqCwBg&oq=&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgwIABDqAhC0AhBDGAEyDAgAEOoCELQCEEMYATIMCAAQ6gIQtAIQQxgBMg8IABDqAhC0AhBDEIsDGAEyDwgAEOoCELQCEEMQiwMYATIYCC4QyAMQ6gIQtAIQQxCLAxCcAxCoAxgCMg8ILhDIAxDqAhC0AhBDGAIyGAguEMgDEOoCELQCEEMQiwMQqAMQnAMYAkoECEEYAFAAWABgrgdoAXABeACAAQCIAQCSAQCYAQCgAQGwARK4AQHAAQHaAQYIARABGAHaAQYIAhABGAg&sclient=gws-wiz-serp',
        'https://www.google.com/search?q=%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D1%8F%D0%B7%D1%8B%D0%BA&newwindow=1&rlz=1C1SQJL_ruRU833RU833&sxsrf=AJOqlzVWzVeABBFfgV_ucwH2kz_PqNDcDQ%3A1679256070096&ei=BmoXZJzBBYnOrgTl_bCoCw&oq=%D0%B0%D0%BD%D0%B3%D0%BB&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgQIIxAnMgcIABCxAxBDMgQIABBDMgQIABBDMgQIABBDMggIABCABBCxAzILCAAQgAQQsQMQgwEyBAgAEEMyBAgAEEMyBAgAEEM6BQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoECC4QQ0oECEEYAFAAWJ0DYPELaABwAXgAgAFZiAGSApIBATSYAQCgAQHAAQE&sclient=gws-wiz-serp']
    assert parser.Parser(r"C:\Users\Roman Andreevich\зфкыукы\test_docs\link.doc").get_links_doc() == true







