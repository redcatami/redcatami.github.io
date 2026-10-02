from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
exclude={'.tools','vendor','_site','.bundle','.jekyll-cache','.git','node_modules','Redcatech-source.zip','.jekyll-metadata'}
dest=root/'Redcatech-source.zip'
with ZipFile(dest,'w',ZIP_DEFLATED) as archive:
    for item in root.iterdir():
        if item.name in exclude:continue
        files=item.rglob('*') if item.is_dir() else [item]
        for file in files:
            if file.is_file():archive.write(file,file.relative_to(root))
with ZipFile(dest) as archive:
    assert '.github/workflows/pages.yml' in archive.namelist()
    assert not any(name.startswith(('.tools/','vendor/','_site/')) for name in archive.namelist())
    print(f'Packaged {len(archive.namelist())} source files: {dest}')
