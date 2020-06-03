import shutil

def copy_arr(src_paths_arr:str, dest_folder:str):
    for s in src_paths_arr:
        dfn = s.split('/')[-1]
        shutil.copy(
            s,
            f'{dest_folder}/{dfn}'
        )
