from pathlib import Path

def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for p in paths:
        path_obj = Path(p)
        name = path_obj.name
        if name.startswith('.') and '.' not in name[1:]:
            ext = ""
        elif '.' not in name:
            ext = ""
        else:
            ext = path_obj.suffix.lower()
            if ext.startswith('.'):
                ext = ext[1:]
                
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    sorted_paths = sorted(paths)
    return max(sorted_paths, key=lambda p: p.count('/'))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    unit_idx = 0
    
    while size >= 1024 and unit_idx < len(units) - 1:
        size /= 1024.0
        unit_idx += 1
        
    if unit_idx == 0:
        return f"{int(size)} {units[unit_idx]}"
    else:
        return f"{size:.1f} {units[unit_idx]}"

