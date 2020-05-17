
import sys


def read_file(filename):
	#read into file and return a list of file lines without the '\n'
    file = open(filename, 'r')
    read_file = file.readlines()  # list containign opened file contents
    file_lines = []
    space = ''
    #print (read_file)

    for line in read_file:
        #line.strip(')')
        #line.strip('[')
        #line.strip(']')
        #line.strip('(')
        #line.strip ('\n')
        #redundant code above
        file_lines.append(line.strip( '[]( )\n')) # takes out the nonsense, i.e newline, extra spaces, brackets e.t.c
        
        #if (line == ' '):
    
    while (file_lines.count(space)):
        file_lines.remove(space) 
    
    print (file_lines)
    file.close()

    return file_lines

def output (songfile,newfile):
    f = open (newfile , 'w')
    
    #line = f.readline
    #print (line)
    i = 0
    
    x = len (songfile)
    while i < x :

    

        
        if (songfile[i].lower().startswith("verse", 0) or songfile[i].lower().startswith("chorus",0 ) or songfile[i].lower().startswith("bridge",0 )):
                f.write (songfile [i] + '\n')
                i = i+1
        
        f.write (songfile [i] + '\n' )


        j = i+1
       
             
            

        if (i < x-1):


            if (songfile[j].lower().startswith("verse",0 ) or songfile[j].lower().startswith("chorus",0 ) or songfile[j].lower().startswith("bridge",0 ) or songfile[j].lower().startswith("interlude",0 )):
                 
                 p = j
                 f.write('\n')
                 
                 f.write(songfile[p] + '\n')

            else :
          
                f.write (songfile[j] + '\n' + '\n')
          
        i = j+1
    f.close()



def main () :

    in_filename = ''
    in_filename = sys.argv[1]
    infile_lines = read_file(in_filename)
    output (infile_lines,in_filename)
    #print (infile_lines)
    


if __name__ == '__main__':
    main()