import os

while True :
    
    folderPath = input("Enter the path of the folder you want to organize: ")
    
    files = os.listdir(folderPath)
    
    extensions = []
    
    for x in files :
        
        if os.path.splitext(x)[1] not in extensions and os.path.splitext(x)[1] != "" :
            
            extensions.append(os.path.splitext(x)[1])
    
    for x in extensions :
        
        newFolder = x[1 : len(x)]
        
        if os.path.isdir(os.path.join(folderPath, newFolder)) == False :
            
            os.mkdir(os.path.join(folderPath, newFolder))
        
        for y in files :
            
            if os.path.splitext(y)[1] == x :
                
                os.rename(os.path.join(folderPath, y), os.path.join(folderPath, newFolder, y))
    
    print("\nFolder was successfully organized!\n\n")
