o
    VcK  ã                   @   s¾   d dl Z d dlZddiZg d¢ZdZdZdZdZd	Zzd dl	Z	W n e
y-   ed
 Y nw zd dlmZ W n e
yC   ed Y nw dd Zdd Zdd Zdd Zedkr]e  dS dS )é    Nz
User-AgentzBMozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0)ÚIDZJPZUSZKRZFRZDEZTWZRUZGBÚNLZCZZTRÚATZCHZESZCAZSEZILZPLZIRZNOZROÚINZVNZBEZBRZBGr   ZDKZARZMXZFIZCNZCLZZAZSKZHUZIEZEGZTHZUAZRSZHKZGRZPTZLVZSGZISZMYZCOZTNZEEZDOZSIZECZLTZPSZNZZBDZPAZMDZNIZMTZTTZSAZHRZCYZPKZAEZKZZKWZVEZGEZMEZSVZLUZCWZPRZCRZBYZALZLIZBAZPYZPHZFOZGTZNPZPEZUYZITZADZAGZAMZAOZAUZAWZAZZBBZBQZBSZBWZCGZCIZDZZFJZGAZGGZGLZGPZGUZGYZHNZJEZJMZJOZKEZKHZKNZKYZLAZLBZLKZMAZMGZMKZMNZMOZMQZMUZNAZNCZNGZQAZREZSDZSNZSRZSTZSYZTZZUGZUZZVCZBJú[1;32mú[0mz[33mz[1;34mz[1;31mzinstall module requests dulu !)Útrackzinstall module rich dulu !c                   C   s   t  d¡ d S )NÚclear)ÚosÚsystem© r   r   õ   ããã¯.pyr	   5   s   r	   c                   C   s<   t t dt dt dt dt dt dt dt d d S )	Nu   ãDUMP SERVER CCTVz
 z 1 >> zIndonesia
 z 2 >> zJepang :v
 z 3 >> zAmerika 
  )ÚprintÚblueÚwhiteÚyellowr   r   r   r   Úmenu7   s   ÿÿþþýýr   c                	   C   s*   t   tt dt dt dt d d S )NuÖ  
 â â â â â â â â â â â â â â â â¢»â£¿â£¶â â â â â â â â â â â 
termuxID
âââââ ââââââ ââââââ âââââ ââââââ 
âââââ ââââââ ââââââ âââââ ââââââ 
âââââ ââââââ ââââââ âââââ ââââââ
â â â â â â â â â â â â â â â â¢»â¡¿â â â â â â â â â â â â â ããã¯
  z"Hacking common CCTV in the world !z
  z,>> CTRL+Z Exit
  RyugenXD Python World :)
  )r	   r   ÚgreenÚmagentor   r   r   r   r   r   Úlogo=   s   ùùør   c                  C   s  t   t  ttd} zbt| d  }tjd| td}t 	d|j
¡d }tt dt  ttt|dd	D ]2}tjd| d
| td}t 	d|j
¡}tt dt|d  dt  |D ]	}td|d  qaq9W d S  tjy}   td Y d S  ty   td Y d S w )NzPILIH : é   z$http://www.insecam.org/en/bycountry/)Úheaderszpagenavigator\("\?page=", (\d+)r   zCRTL+C untuk KeluarzPROSES DUMP CCTV...)Údescriptionz/?page=zhttp://\d+.\d+.\d+.\d+:\d+zDUMP SERVER ú r   r   zKoneksi Internet Error !zBerhasil Keluar Dari program !)r   r   ÚintÚinputÚ	countriesÚrequestsÚgetr   ÚreÚfindallÚtextr   r   r   r   Úranger   ÚstrÚConnectionErrorÚexitÚKeyboardInterrupt)ZnumZcountryÚresZ	last_pageZpageZfind_ipZipr   r   r   ÚmainK   s*    ÿüÿr(   Ú__main__)r
   r   r   r   r   r   r   r   r   r   ÚModuleNotFoundErrorr%   Zrich.progressr   r	   r   r   r(   Ú__name__r   r   r   r   Ú<module>   s2   $ÿÿ
ÿ