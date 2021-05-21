import csv
import jinja2


env = jinja2.Environment(
    block_start_string='<%',
    block_end_string='%>',
    variable_start_string='<<',
    variable_end_string='>>',
    comment_start_string='!!!',
    comment_end_string='!!!',
    loader=jinja2.FileSystemLoader('.'),
)


if __name__ == "__main__":
    with open("kems.csv", "r") as kemsfile:
        reader = csv.DictReader(kemsfile)
        kems = [row for row in reader]

    with open("sigs.csv", "r") as sigsfile:
        reader = csv.DictReader(sigsfile)
        sigs = [row for row in reader]

    template = env.get_template("kems.tex.j2")
    with open("kems.tex", "w") as kemfile:
        kemfile.write(template.render(kems=kems))

    template = env.get_template("kemsoverview.tex.j2")
    with open("kemsoverview.tex", "w") as overviewfile:
        overviewfile.write(template.render(kems=kems))

    template = env.get_template("sigs.tex.j2")
    with open("sigs.tex", "w") as kemfile:
        kemfile.write(template.render(sigs=sigs))

    template = env.get_template("sigsoverview.tex.j2")
    with open("sigsoverview.tex", "w") as overviewfile:
        overviewfile.write(template.render(sigs=sigs))
