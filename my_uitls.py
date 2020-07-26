import shutil

def copy_arr(src_paths_arr:str, dest_folder:str, prefix:str='')->None:
    for s in src_paths_arr:
        dfn = s.split('/')[-1]
        if prefix:
          ext, dfn = dfn[::-1].split('.',maxsplit=1)
          ext, dfn = ext[::-1], dfn[::-1]
          dfn = f'{prefix}_{dfn}.{ext}'
        shutil.copy(
            s,
            f'{dest_folder}/{dfn}'
        )
