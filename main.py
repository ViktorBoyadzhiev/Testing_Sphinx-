#file:///C:/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/index.html

import pdfgen


async def f():
    pass
    # ## FOR WEBITES
    # await pdfgen.from_url('http://google.com', 'out.pdf')

    # ## FOR HTML FILES
    # await pdfgen.from_file('file:///C:/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/index.html', 'out.pdf')

    # ## FOR TEXT FILES
    # await pdfgen.from_string('Hello!', 'out.pdf')

pdfgen.from_file('file:///C:/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/index.html', 'file:///C:/Users/vby/PycharmProjects/Testing_Sphinx-/docs/_build/html/out.pdf')


