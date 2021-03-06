from bioruler.library.exporters import KappaExporter
from bioruler.library.importers import KappaImporter

import argparse
parser = argparse.ArgumentParser(description='Test translator')
parser.add_argument('-pars', dest='pars', action='store', type=str,
                    default=None, help='parser path')
parser.add_argument('-p', dest='p', action='store_const', const=True,
                    default=False, help='print results')
args = parser.parse_args()

if args.pars is None:
    args.pars = "bioruler/library/kappa_to_graph.byte"

# open kappa file

in_file = open('test.ka', 'r')

# uncompile kappa file using args.pars as parser, imported is a nugget list, imported[i].metamodel_ is their action graph and imported[î].hom is a valid homomorphism between the i-th nugget and the action graph

imported = KappaImporter.uncompile(["test.ka"], parser=args.pars)

# compile back the nuggets into rules

compiled = KappaExporter.compile_nugget_list(imported)

if args.p:
    f = open('res.txt', 'a+')
    print("---------------------------- Original\n\n%s" % in_file.read(), file=f)

    print("---- Result :\n\n"+"\n\n".join(compiled)+"\n---------------------------- End\n\n", file=f)

else:

    print("---------------------------- Original\n\n%s" % in_file.read())

    print("---- Result :\n\n"+"\n\n".join(compiled)+"\n---------------------------- End\n\n")
