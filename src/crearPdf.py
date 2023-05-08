import jinja2
import pdfkit

def create_pdf(path_template, info, path_css=''):
    name_template = path_template.split('/')[-1]
    path_template = path_template.replace(name_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(path_template))
    template = env.get_template(name_template)
    html = template.render(info)
    
    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': 'UTF-8'
    }

    config = pdfkit.configuration(wkhtmltopdf='C:/ProgramData/chocolatey/bin/wkhtmltopdf.exe')
    path_output = 'C:/Users/User/Documents/Repos/Invoice-Platform-SB/output/template_filled.pdf'
    pdfkit.from_string(html, path_output, options=options, configuration=config) #css= |  

if __name__ == "__main__":
    path_template = 'C:/Users/User/Documents/Repos/Invoice-Platform-SB/templates/template.html'
    info = {"firstName": "Arath", "lastName": "Burgos"}
    create_pdf(path_template, info)