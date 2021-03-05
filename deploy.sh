#!/usr/bin/env sh

programs=(
"mpd"
"ncmpcpp"
"ranger"
"rofi"
"terminator"
"dunst"
"zathura"
"mpv"
"qutebrowser"
"sxhkd"
".toprc"
".bashrc"
".gitconfig"
".tmux.conf"
".xprofile"
".bash_profile"
".xinitrc"
".xsession"
".url_handler"
".extract_urlview"
".Xresources"
)

for d in ${programs[@]}
do
	DEFAULT_DIR="$HOME/.config/$d"
	# all the .XXX config file goes to the $HOME/
	if [ `echo $d | grep "^\."` ]
	then
		[ -f ~/$d ] && rm -rvf ~/$d
		ln -s $PWD/dotfile/dot_${d##.} ~/$d
	else # individual setup directory goes to the $HOME/.config/
		[ -d $DEFAULT_DIR ] && rm -rvf $DEFAULT_DIR
		ln -s $PWD/$d $HOME/.config/$d
	fi
done
