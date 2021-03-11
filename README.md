# Gentoo Rice(All the setup for my gentoo linux)

## Basic Comcept

### xprofile

~/.xprofile和/etc/xprofile的加载顺序在X session前即在(WindowManager)前

xprofile被下面的DisplayManager加载

- GDM(/etc/gdm/Xsession)
- LightDM(/etc/lightdm/Xsession)
- LXDM(/etc/lxdm/Xsession)
- SDDM

如果使用了DM的情况下加载顺序如下

	DM--> source xprofile --> WM

如果不使用DM的话xprofile还可以被下面程序加载

- startx
- xinit
- XDM
- 其他使用~/.xsession或~/.xinitrc的DM

~/.xinitrc and /etc/X11/xinit/xinitrc

	#!/bin/sh

	# Make sure this is before the 'exec' command or it won't be sourced.
	[ -f /etc/xprofile ] && . /etc/xprofile
	[ -f ~/.xprofile ] && . ~/.xprofile

### 使用startx来启动xinitrc

login fromm tty1 work flow(Xresources should load before i3wm)

	.bash_profile ==> startx ==> .xinitrc ==> i3wm

## xdg-utils

如下的相关文件都记录xdg-open默认使用什么程序打开文件

	/usr/share/applications/mimeapps.list
	/usr/share/applications/mimeinfo.cache
	~/.local/share/applications/defaults.list
	~/.local/share/applications/mimeapps.list
	~/.local/share/applications/mimeinfo.cache

查看pdf文件的分类

	file -i file.pdf
	application/pdf; charset=binary

查询打开这个分类的默认应用程序

	xdg-mime query default application/pdf

想要让xdg-open默认使用zathura来打开(修改上述文件中的内容如下)

	application/pdf=org.pwmt.zathura-pdf-mupdf.desktop;

## Download and Install

Download the source code

	git clone https://github.com/54shady/grice.git ~/.grice

Install Tmux Plugin Manager

	git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

## Make Links

Make links to the target file using [deply.sh](deploy.sh)

## Do web search in terminal

Quick search in terminal using hotkey 's'

	ln -s ~/.grice/bin/web_search ~/.grice/bin/s

Export the path of tools directory

Example for search "gentoo linux"

	$ s gentoo linux

## Quick translate in terminal

Make a link(the first charactor of translate)

	ln -s ~/.grice/bin/youdaofanyi.py ~/.grice/bin/t

Translate using youdao online dictionary

	$ t hello world
	$ t 'have a nice day'

## MailBox setup

mail info

	name: demo@163.com
	password: mypass

mutt

	ln -s ~/.grice/dotfile/dot_muttrc ~/.muttrc
	sed -i 's/yournamegoeshere/realname/' ~/.grice/dotfile/dot_muttrc
	sed -i 's/name@server/demo@163.com/' ~/.grice/dotfile/dot_muttrc

getmail(执行getmail收取邮件 可以写入crontab)

	ln -s ~/.grice/getmail ~/.getmail
	sed -i 's/name@server/demo@163.com/' ~/.grice/getmail/getmailrc
	sed -i 's/pass-for-demo/mypass/' ~/.grice/getmail/getmailrc

使用sys-process/cronie来定时执行

	sudo crond
	crontab -e

每一分钟收取一次邮件

	* * * * * /usr/bin/getmail &> /dev/null

msmtp

	ln -s ~/.grice/dotfile/dot_msmtprc ~/.msmtprc
	chmod 600 ~/.msmtprc
	sed -i 's/name@server/demo@163.com/' ~/.grice/dotfile/dot_msmtprc
	sed -i 's/pass-for-demo/mypass/' ~/.grice/dotfile/dot_msmtprc

Microsoft Exchange Server(Using DavMail as gateway)

邮件服务器是微软Exchange的话可以使用DavMail来作本地代理服务器

DavMail default port

	SMTP 1025
	POP 1110
	IMAP 1143
	CALDAV 1080
	LDAP 1389

getmail可以配置多个配置文件来同时接收多个邮箱的邮件

	getmail -r /path/to/getmailrc-davmail
