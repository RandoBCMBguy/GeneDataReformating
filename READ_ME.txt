Open source alignment or phylogeny programs such as muscle and phylogeny.fr display accession numbers rather than organism/gene/protein
names. This makes analyzed data difficult to interpret. My program reformats the info lines (denoted by > characters) so that the 
accession numbers and organism name are switched. The programs will then display the organism name, saving the researcher the effort of
manually changing every accession number in the text file before uploading to the program. 

To use, download all programs in one directory. Create a new, empty text file that you want to write the edited fasta file to.
Write a new file, import ReformatFasta.py, and run ReformatFasta(originalFile,newFile) with the originalFile being the directory of your
gene/protein information dump in fasta format, and newFile being the empty text file. Then upload your previously empty text file to
MUSCLE or phylogeny.fr or whatever and enjoy not having to arduously edit each name by hand.
