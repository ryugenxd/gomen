o
    ��VcK  �                   @   s�   d dl Z d dlZddiZg d�ZdZdZdZdZd	Zzd dl	Z	W n e
y-   ed
� Y nw zd dlmZ W n e
yC   ed� Y nw dd� Zdd� Zdd� Zdd� Zedkr]e�  dS dS )�    Nz
User-AgentzBMozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0)��IDZJPZUSZKRZFRZDEZTWZRUZGB�NLZCZZTR�ATZCHZESZCAZSEZILZPLZIRZNOZRO�INZVNZBEZBRZBGr   ZDKZARZMXZFIZCNZCLZZAZSKZHUZIEZEGZTHZUAZRSZHKZGRZPTZLVZSGZISZMYZCOZTNZEEZDOZSIZECZLTZPSZNZZBDZPAZMDZNIZMTZTTZSAZHRZCYZPKZAEZKZZKWZVEZGEZMEZSVZLUZCWZPRZCRZBYZALZLIZBAZPYZPHZFOZGTZNPZPEZUYZITZADZAGZAMZAOZAUZAWZAZZBBZBQZBSZBWZCGZCIZDZZFJZGAZGGZGLZGPZGUZGYZHNZJEZJMZJOZKEZKHZKNZKYZLAZLBZLKZMAZMGZMKZMNZMOZMQZMUZNAZNCZNGZQAZREZSDZSNZSRZSTZSYZTZZUGZUZZVCZBJ�[1;32m�[0mz[33mz[1;34mz[1;31mzinstall module requests dulu !)�trackzinstall module rich dulu !c                   C   s   t �d� d S )N�clear)�os�system� r   r   �   ハック.pyr	   5   s   r	   c                   C   s<   t t� dt� dt� dt� dt� dt� dt� dt� d�� d S )	Nu   〆DUMP SERVER CCTVz
 z 1 >> zIndonesia
 z 2 >> zJepang :v
 z 3 >> zAmerika 
  )�print�blue�white�yellowr   r   r   r   �menu7   s   ������r   c                	   C   s*   t �  tt� dt� dt� dt� d�� d S )Nu�  
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
termuxID
▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ 
▒█░▄▄ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ 
▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█
⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⢻⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ハック
  z"Hacking common CCTV in the world !z
  z,>> CTRL+Z Exit
  RyugenXD Python World :)
  )r	   r   �green�magentor   r   r   r   r   r   �logo=   s   ���r   c                  C   s  t �  t�  ttd��} zbt| d  }tjd|� �td�}t�	d|j
�d }tt� dt� �� ttt|��dd	�D ]2}tjd|� d
|� �td�}t�	d|j
�}tt� dt|d �� dt� �� |D ]	}td|d � qaq9W d S  tjy}   td� Y d S  ty�   td� Y d S w )NzPILIH : �   z$http://www.insecam.org/en/bycountry/)�headerszpagenavigator\("\?page=", (\d+)r   zCRTL+C untuk KeluarzPROSES DUMP CCTV...)�descriptionz/?page=zhttp://\d+.\d+.\d+.\d+:\d+zDUMP SERVER � r   r   zKoneksi Internet Error !zBerhasil Keluar Dari program !)r   r   �int�input�	countries�requests�getr   �re�findall�textr   r   r   r   �ranger   �str�ConnectionError�exit�KeyboardInterrupt)ZnumZcountry�resZ	last_pageZpageZfind_ipZipr   r   r   �mainK   s*    ���r(   �__main__)r
   r   r   r   r   r   r   r   r   r   �ModuleNotFoundErrorr%   Zrich.progressr   r	   r   r   r(   �__name__r   r   r   r   �<module>   s2   $��
�