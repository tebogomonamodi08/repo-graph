'''
This module takes file path as input and returns stuctured 
JSON output, here is the output contract. 
{'repo_name':'...',
 'files':[
     {'name':'...',
     'content':'...',
     'type':'...',
     'path':'...'}
 ]
}

Assumptions:
1. repo exists
2. the url is correct

'''
import os

def ingest(repo : str) -> dict:
  #map os.walk(repo)->(root, dirs, files)
  #returns a stream object
  trace = [ ]  #store logs in for the system
  '''
  repo path(validation will be handled by the frontend)
     |   
  traveral engine(file exists, file is readable, encoding is stable)
     |
  filtering layer(big files will make the system slow for example binary large files)
     |
  structure construction
  '''


  if os.path.exists(repo):
    results = {
      'repo_name': os.path.basename(repo),
      'files': []
    
    }
    for root, dirs, files in os.walk(repo):
      if '.git' in root:
        continue
      
      for f in files:
       #########filtering layer#######################
        f_path = os.path.join(root, f)
        file_size = os.path.getsize(f_path)
        if file_size>1_000_000  or f[0]=='.':
          continue
        ###########################################
        
        
        
        _, ext = os.path.splitext(f_path) #return the extention and path of each file
        content = None #initial state of the content
        error = None
        
        #failure mode handler 
        try:
          with open(f_path, encoding= 'utf-8') as obj:
            content = obj.read()
            
            if content == '':
              status = 'empty'
            else:
              status = 'success'
        except Exception as e:
          status = 'failed'
          error = str(e)
          
        trace.append({'file':f_path,
                      'status': status,
                      'error':error})

          
    
          
        results['files'].append({
            'name': os.path.basename(f),
            'path': f_path,
            'extension': ext.strip('.'),
            'content': content,
            'status': status,
            'relative_path': os.path.relpath(f_path)
            })
        
    
        
      
    return results, trace
    

  else:
    error = 'repo not found in the system.'
    trace.append({
      'file':repo,
      'status':'failed',
      'error': error
    })
    
    return None, trace
    

if __name__=="__main__":
    path = r'C:\Users\Tebogo\OneDrive - Linkfields innovations\Desktop\observability_tool\test\test_repo'
    print(ingest(path))
