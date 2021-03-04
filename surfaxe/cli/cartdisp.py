# Misc 
from argparse import ArgumentParser
import yaml
import os
import warnings 

# Surfaxe 
from surfaxe.analysis import cart_displacements

def _get_parser(): 
    parser = ArgumentParser(
        description="""Produces a txt file with the magnitudes of displacements 
        of atoms during the relaxation. """
    )

    parser.add_argument('-s', '--start', default='POSCAR',
    help=('Filename of structure file in any format supported by pymatgen '
          '(default: POSCAR) '))
    parser.add_argument('-e', '--end', default='CONTCAR',
    help=('Filename of structure file in any format supported by pymatgen. '
    '(default: CONTCAR)'))
    parser.add_argument('-a', '--atoms', default=None, nargs='+', type=str,
    help='List of elements in the structure in any order e.g. Y Ti O S')
    parser.add_argument('--max-disp', type=float, default=0.1, dest='max_disp', 
    help='The maximum displacement shown (default: 0.1)')
    parser.add_argument('--no-txt', default=True, action='store_false', 
    dest='save_txt', help='Prints data to terminal' )
    parser.add_argument('--txt-fname', default='cart_displacament.txt', type=str,
    dest='txt_fname', help=('Filename of the txt file (default: '
         'cart_displacement.txt)'))
    parser.add_argument('--yaml', default=False, action='store_true', 
    help=('Read all args from surfaxe_config.yaml file. Completely overrides any '
    'other flags set '))

    return parser 

def main(): 
    args = _get_parser().parse_args()

    if args.yaml==True: 
        with open('surfaxe_config.yaml', 'r') as y: 
            yaml_args = yaml.safe_load(y)

        cd = cart_displacements(**yaml_args)
        if ('save_csv', False) in yaml_args.items(): 
            print(cd)
 
    else: 
        cd = cart_displacements(args.start, args.end, args.atoms, 
        max_disp=args.max_disp, save_txt=args.save_txt, 
        txt_fname=args.txt_fname)
        
        if args.save_txt: 
            print(cd)

if __name__ == "__main__":
    main()