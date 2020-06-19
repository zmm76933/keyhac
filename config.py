﻿# -*- mode: python; coding: utf-8-with-signature-dos -*-

##                               nickname: Fakeymacs
##
## Windows の操作を Emacs のキーバインドで行うための設定（Keyhac版）ver.20200619_01
##

# このスクリプトは、Keyhac for Windows ver 1.82 以降で動作します。
#   https://sites.google.com/site/craftware/keyhac-ja
# スクリプトですので、使いやすいようにカスタマイズしてご利用ください。
#
# この内容は、utf-8-with-signature-dos の coding-system で config.py の名前でセーブして
# 利用してください。
#
# 本設定を利用するための仕様は、以下を参照してください。
#
# ＜共通の仕様＞
# ・emacs_tareget_class 変数、not_emacs_target 変数、ime_target 変数で、Emacsキーバインドや
#   IME の切り替えキーバインドの対象とするアプリケーションソフトを指定できる。
# ・not_clipboard_target 変数で、clipboard 監視の対象外とするアプリケーションソフトを指定
#   できる。
# ・左右どちらの Ctrlキーを使うかを side_of_ctrl_key 変数で指定できる。
# ・左右どちらの Altキーを使うかを side_of_alt_key 変数で指定できる。
# ・キーバインドの定義では次の表記が利用できる。
#   ・S-    : Shiftキー
#   ・C-    : Ctrlキー
#   ・A-    : Altキー
#   ・M-    : Altキー と Esc、C-[ のプレフィックスキーを利用する３パターンを定義
#             （Emacsキーバインド設定で利用可。emacs の Meta と同様の意味。）
#   ・Ctl-x : ctl_x_prefix_key 変数で定義されているプレフィックスキーに置換え
#             （Emacsキーバインド設定で利用可。変数の意味は以下を参照のこと。）
#   ・(999) : 仮想キーコード指定
#
# ＜Emacsキーバインド設定と IME の切り替え設定を有効にしたアプリケーションソフトでの動き＞
# ・toggle_input_method_key 変数と set_input_method_key 変数の設定により、IME を切り替える
#   キーを指定できる。
# ・use_emacs_ime_mode 変数の設定により、Emacs日本語入力モードを使うかどうかを指定
#   できる。Emacs日本語入力モードは、IME が ON の時に文字（英数字かスペースを除く
#   特殊文字）を入力すると起動する。
#   Emacs日本語入力モードでは、次のキーのみが Emacsキーバインドとして利用でき、
#   その他のキーは emacs_ime_mode_key 変数に設定したキーにより置き換えがされた後、
#   Windows にそのまま渡されるようになる。
#   ・Emacs日本語入力モードで使える Emacsキーバインドキー
#     ・C-[
#     ・C-b、C-f
#     ・C-p、C-n
#     ・C-a、C-e
#     ・C-h
#     ・C-d
#     ・C-m
#     ・C-g
#     ・scroll_key 変数で指定したスクロールキー
#   Emacs日本語入力モードは、次の操作で終了する。
#   ・Enter、C-m または C-g が押された場合
#   ・[半角／全角] キー、A-` キーが押された場合
#   ・BS、C-h 押下直後に toggle_input_method_key 変数や set_input_method_key 変数の
#     disable で指定したキーが押された場合
#     （間違って日本語入力をしてしまった時のキー操作を想定しての対策）
# ・Emacs日本語入力モードの使用を有効にした際、emacs_ime_mode_balloon_message 変数の
#   設定でバルーンメッセージとして表示する文字列を指定できる。
# ・use_emacs_shift_mode 変数の設定により、Emacsシフトモードを使うかどうかを指定できる。
#   Emacsシフトモードを使う場合は次の動きとなる。
#   ・C-[a-z]キーを Shiftキーと一緒に押した時は、Shiftキーをとったキー（C-[a-z]）が
#     Windows に入力される。
#   ・A-[a-z]キーを Shiftキーと一緒に押した時は、Shiftキーをとったキー（A-[a-z]）が
#     Windows に入力される。
#
# ＜Emacsキーバインド設定を有効にしたアプリケーションソフトでの動き＞
# ・use_ctrl_i_as_tab 変数の設定により、C-iキーを Tabキーとして使うかどうかを指定できる。
# ・use_esc_as_meta 変数の設定より、Escキーを Metaキーとして使うかどうかを指定できる。
#   use_esc_as_meta 変数が True（Metaキーとして使う）に設定されている場合、ESC の
#   二回押下で ESC が入力される。
# ・ctl_x_prefix_key 変数の設定により、Ctl-xプレフィックスキーに使うキーを指定できる。
# ・scroll_key 変数の設定により、スクロールに使うキーを指定できる。scroll_key 変数を
#   None に設定するなどして C-v の指定を外すと、C-v が Windows の 「ペースト」として
#   機能するようになる。
# ・C-c、C-/ は、Windows の「コピー」、「取り消し」が機能するようにしている。
#   ctl_x_prefix_key 変数が C-x 以外に設定されている場合には、C-x が Windows の
#   「カット」として機能するようにしている。
# ・C-k を連続して実行しても、クリップボードへの削除文字列の蓄積は行われない。
#   複数行を一括してクリップボードに入れたい場合は、削除の範囲をマークして削除するか
#   前置引数を指定して削除する。
# ・C-y を前置引数を指定して実行すると、ヤンク（ペースト）の繰り返しが行われる。
# ・C-l は、アプリケーションソフト個別対応とする。recenter 関数で個別に指定すること。
#   この設定では、Sakura Editor のみ対応している。
# ・キーボードマクロの再生時に IME の状態に依存した動作とならないようにするため、
#   キーボードマクロの記録と再生の開始時に IME を強制的に OFF にするようにしている。
# ・kill-buffer に Ctl-x k とは別に M-k も割り当てている。プラウザのタブを削除する際
#   などに利用可。
# ・use_ctrl_digit_key_for_digit_argument 変数の設定により、数引数の指定に Ctrl+数字
#   キーを使うかを指定できる。
# ・reconversion_key 変数の設定により、IME の「再変換」を行うキーを指定できる。
#
# ＜全てのアプリケーションソフトで共通の動き＞
# ・use_alt_digit_key_for_f1_to_f12 の設定により、F1 から F12 を Alt+数字キー列として
#   使うかを指定できる。
# ・use_alt_shift_digit_key_for_f13_to_f24 の設定により、F13 から F24 を Alt+Shift+数字
#   キー列として使うかを指定できる。
# ・other_window_key 変数に設定したキーにより、表示しているウィンドウの中で、一番最近
#   までフォーカスがあったウィンドウに移動する。NTEmacs の機能やランチャーの機能から
#   Windows アプリケーションソフトを起動した際に、起動元のアプリケーションソフトに戻る
#   のに便利。この機能は Ctl-x o にも割り当てているが、こちらは Emacs のキーバインドを
#   適用したアプリケーションソフトのみで有効となる。
# ・clipboardList_key 変数に設定したキーにより、クリップボードリストが起動する。
#   （C-f、C-b でリストの変更、C-n、C-p でリスト内を移動し、Enter で確定する。
#     C-s、C-r で検索も可能。migemo 辞書を登録してあれば、検索文字を大文字で始める
#     ことで migemo 検索も可能。Emacsキーバインドを適用しないアプリケーションソフト
#     でもクリップボードリストは起動し、選択した項目を Enter で確定することで、
#     クリップボードへの格納（テキストの貼り付けではない）が行われる。）
# ・lancherList_key 変数に設定したキーにより、ランチャーリストが起動する。
#   （全てのアプリケーションソフトで利用可能。操作方法は、クリップボードリストと同じ。）
# ・クリップボードリストやランチャーリストのリストボックス内では、基本、Altキーを
#   Ctrlキーと同じキーとして扱っている。（C-v と A-v の置き換えのみ行っていない。）
# ・window_switching_key 変数に設定したキーにより、アクティブウィンドウの切り替えが行われる。
# ・マルチディスプレイを利用している際に、window_movement_key_for_displays 変数に設定した
#   キーにより、アクティブウィンドウのディスプレイ間の移動が行われる。
# ・window_minimize_key 変数に設定したキーにより、ウィンドウの最小化、リストアが行われる。
# ・desktop_switching_key 変数に設定したキーにより、仮想デスクトップの切り替えが行われる。
#   （仮想デスクトップの利用については、次のページを参照ください。
#     ・http://pc-karuma.net/windows-10-virtual-desktops/
#     ・http://pc-karuma.net/windows-10-virtual-desktop-show-all-window-app/
#     仮想デスクトップ切替時のアニメーションを止める方法は次のページを参照ください。
#     ・http://www.jw7.org/2015/11/03/windows10_virtualdesktop_animation_off/ ）
# ・window_movement_key_for_desktops 変数に設定したキーにより、アクティブウィンドウの
#   仮想デスクトップ間の移動が行われる。
#   （本機能を利用する場合は、Microsoft Store から SylphyHorn をインストールしてください。）
# ・word_register_key 変数に設定したキーにより、IME の「単語登録」プログラムの起動が
#   行われる。

import time
import sys
import os.path
import re
import fnmatch
import copy
import ctypes

import keyhac_keymap
from keyhac import *

def configure(keymap):

    ####################################################################################################
    ## キーの置き換え（KeySwap を使わない場合。ただし、CapsLock の置き換えは KeySwap で行う必要あり。）
    ####################################################################################################

    # https://w.atwiki.jp/ntemacs/pages/90.html

    # 初代 HHKB で Mode SW を 3 にした場合のお勧め設定
    # （Ctrl+Alt+Del は置き換える前のキーの配置で押下する必要があるようです）
    # （Win+L も効かなくなるようですので、Ctrl+Win(元Alt)+Del -> ロック をご利用ください）
    if 0:
        keymap.replaceKey("LAlt", "LWin")
        keymap.replaceKey("RAlt", "RCtrl")
        keymap.replaceKey(235, "LAlt")           # 左◇キーを LAlt キーにする
        keymap.replaceKey(255, "RAlt")           # 右◇キーを RAlt キーにする

    # HHKB Pro2 の Lite拡張モードで DIP SW 4 を OFF、DIP SW 5 を ON にした場合のお勧め設定
    if 0:
        keymap.replaceKey("RWin", "RCtrl")       # RAlt の位置のキーを RCtrl キーにする

    # OS の設定を英語キーボードにして日本語キーボードを利用する場合のお勧め設定
    # （Change Key を使って、[￥] キーにスキャンコード 0x7F を割り当ててから、以下の設定を有効
    # 　にしてください）
    if 0:
        keymap.replaceKey(235, 29)               # [無変換] キーを OS が認識可能なキーにする
        keymap.replaceKey(255, 28)               # [変換] キーを OS が認識可能なキーにする
        keymap.replaceKey(193, "RShift")         # [＼] キーを RShift キーにする
        keymap.replaceKey(236, "BackSlash")      # [￥] キーを BackSlash キーにする
        keymap.replaceKey("BackSlash", "Return") # [ ]] キーを Enter キーにする

        # （リモートデスクトップで接続する場合など、一つの OS を英語キーボードと日本語キーボード
        # 　とで混在して利用することがあります。この場合、一部の設定の切り替えが必要となるため、
        # 　その設定を本設定の最後に「（オプション）」として紹介しています。）


    ####################################################################################################
    ## カスタマイズの設定
    ####################################################################################################

    # OS に設定しているキーボードタイプが日本語キーボードかどうかを設定する（自動設定）
    # （True: 日本語キーボード、False: 英語キーボード）
    # （ http://tokovalue.jp/function/GetKeyboardType.htm ）
    if ctypes.windll.user32.GetKeyboardType(0) == 7:
        is_japanese_keyboard = True
    else:
        is_japanese_keyboard = False

    # Emacs のキーバインドにするウィンドウのクラスネームを指定する（全ての設定に優先する）
    emacs_target_class   = ["Edit"]                   # テキスト入力フィールドなどが該当

    # Emacs のキーバインドに“したくない”アプリケーションソフトを指定する
    # （Keyhac のメニューから「内部ログ」を ON にすると processname や classname を確認することができます）
    not_emacs_target = ["bash.exe",               # WSL
                        "ubuntu.exe",             # WSL
                        "ubuntu1604.exe",         # WSL
                        "ubuntu1804.exe",         # WSL
                        "ubuntu2004.exe",         # WSL
                        "debian.exe",             # WSL
                        "kali.exe",               # WSL
                        "SLES-12.exe",            # WSL
                        "openSUSE-42.exe",        # WSL
                        "openSUSE-Leap-15-1.exe", # WSL
                        "mstsc.exe",              # Remote Desktop
                        "WindowsTerminal.exe",    # Windows Terminal
                        "mintty.exe",             # mintty
                        "Cmder.exe",              # Cmder
                        "ConEmu.exe",             # ConEmu
                        "ConEmu64.exe",           # ConEmu
                        "emacs.exe",              # Emacs
                        "emacs-X11.exe",          # Emacs
                        "emacs-w32.exe",          # Emacs
                        "gvim.exe",               # GVim
                        "Code.exe",               # VSCode
                        "devenv.exe",             # Visual Studio
                        "xyzzy.exe",              # xyzzy
                        "VirtualBox.exe",         # VirtualBox
                        "XWin.exe",               # Cygwin/X
                        "XWin_MobaX.exe",         # MobaXterm/X
                        "Xming.exe",              # Xming
                        "vcxsrv.exe",             # VcXsrv
                        "X410.exe",               # X410
                        "putty.exe",              # PuTTY
                        "ttermpro.exe",           # TeraTerm
                        "MobaXterm.exe",          # MobaXterm
                        "TurboVNC.exe",           # TurboVNC
                        "vncviewer.exe",          # UltraVNC
                        "vncviewer64.exe",        # UltraVNC
                        "TeamViewer.exe",         # TeamViewer
                        "Xpra-Launcher.exe",      # Xpra
                       ]

    # IME の切り替え“のみをしたい”アプリケーションソフトを指定する
    # （指定できるアプリケーションソフトは、not_emacs_target で（除外）指定したものからのみとなります）
    ime_target           = ["bash.exe",               # WSL
                            "ubuntu.exe",             # WSL
                            "ubuntu1604.exe",         # WSL
                            "ubuntu1804.exe",         # WSL
                            "ubuntu2004.exe",         # WSL
                            "debian.exe",             # WSL
                            "kali.exe",               # WSL
                            "SLES-12.exe",            # WSL
                            "openSUSE-42.exe",        # WSL
                            "openSUSE-Leap-15-1.exe", # WSL
                            "WindowsTerminal.exe",    # Windows Terminal
                            "mintty.exe",             # mintty
                            "Cmder.exe",              # Cmder
                            "ConEmu.exe",             # ConEmu
                            "ConEmu64.exe",           # ConEmu
                            "gvim.exe",               # GVim
                            "Code.exe",               # VSCode
                            "devenv.exe",             # Visual Studio
                            "xyzzy.exe",              # xyzzy
                            "putty.exe",              # PuTTY
                            "ttermpro.exe",           # TeraTerm
                            "MobaXterm.exe",          # MobaXterm
                   ]

    # clipboard 監視の対象外とするアプリケーションソフトを指定する
    not_clipboard_target = ["EXCEL.EXE"]              # Excel

    # 左右どちらの Ctrlキーを使うかを指定する（"L": 左、"R": 右）
    side_of_ctrl_key = "L"

    # 左右どちらの Altキーを使うかを指定する（"L": 左、"R": 右）
    side_of_alt_key = "L"

    # 左右どちらの Winキーを使うかを指定する（"L": 左、"R": 右）
    side_of_win_key = "L"

    # C-iキーを Tabキーとして使うかどうかを指定する（True: 使う、False: 使わない）
    use_ctrl_i_as_tab = False

    # Escキーを Metaキーとして使うかどうかを指定する（True: 使う、False: 使わない）
    use_esc_as_meta = False

    # C-[キーを MultiStrokeキーとして使うかどうかを指定する（True: 使う、False: 使わない）
    use_multi_stroke_open_bracket_as_esc = False

    # Ctl-xプレフィックスキーに使うキーを指定する
    # （Ctl-xプレフィックスキーのモディファイアキーは、Ctrl または Alt のいずれかから指定してください）
    ctl_x_prefix_key = "C-x"

    # スクロールに使うキーの組み合わせ（Up、Down の順）を指定する
    # scroll_key = None # PageUp、PageDownキーのみを利用する
    scroll_key = ["C-z", "M-v", "C-v"]

    # Emacs日本語入力モードを使うかどうかを指定する（True: 使う、False: 使わない）
    use_emacs_ime_mode = False

    # Emacs日本語入力モードが有効なときに表示するバルーンメッセージを指定する
    emacs_ime_mode_balloon_message = None
    # emacs_ime_mode_balloon_message = "▲"

    # Emacsシフトモードを使うかどうかを指定する（True: 使う、False: 使わない）
    use_emacs_shift_mode = False

    # IME をトグルで切り替えるキーを指定する（複数指定可）
    toggle_input_method_key = []
    toggle_input_method_key += ["C-Yen"]
    # toggle_input_method_key += ["C-o"]
    # toggle_input_method_key += ["O-LAlt"]

    #---------------------------------------------------------------------------------------------------
    # IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する（複数指定可）
    # （toggle_input_method_key のキー設定より優先します）
    set_input_method_key = []

    ## 日本語キーボードを利用している場合、[無変換] キーで英数入力、[変換] キーで日本語入力となる
    set_input_method_key += [["(29)", "(28)"]]

    ## LAlt のワンショットモディファイアで英数入力、RAlt のワンショットモディファイアで日本語入力となる
    # set_input_method_key += [["O-LAlt", "O-RAlt"]]

    ## C-j や C-j C-j で 英数入力となる（toggle_input_method_key の設定と併せ、C-j C-o で日本語入力となる）
    # set_input_method_key += [["C-j", None]]

    ## C-j で英数入力、C-o で日本語入力となる（toggle_input_method_key の設定より優先）
    # set_input_method_key += [["C-j", "C-o"]]
    #---------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------------------
    # IME の「再変換」を行うキーを指定する

    ## IME の「再変換」のために利用するキーを設定する（複数指定可）
    reconversion_key = []
    reconversion_key += ["C-t"]
    # reconversion_key += ["C-Back"] # C-t を Chrome のショートカットキーとして使いたい場合の代替え案
    # reconversion_key += ["(28)"]   # [変換] キーを利用する場合でも、本機能を全て使うためには設定が必要
    # reconversion_key += ["O-RAlt"] # ワンショットモディファイアの指定も可能

    ## IME に設定してある「再変換」、「確定取り消し」を行うキーを指定する

    ## Windows 10 1909 以前の Microsoft IME の場合
    ## （Windows 10 1909 以前の Microsoft IME の場合、C-t を押下して確定の取り消しの状態に入った後、
    ## 　Ctrl キーを押したままで C-n による選択メニューの移動を行おうとすると正常に動作しません。
    ## 　一度 Ctrl キーを離す、メニューの移動に Space キーを利用する、reconversion_key に設定する
    ## 　キーを Ctrl キーと組み合わせない、ime_cancel_key に "W-Slash" を設定して「再変換」の機能
    ## 　として利用するなど、いくつかの回避方法があります。お試しください。）
    if 1:
        ime_reconv_key = "W-Slash" # 「再変換」キー
        ime_cancel_key = "C-Back"  # 「確定の取り消し」キー
        ime_reconv_region = False  # 「再変換」の時にリージョンの選択が必要かどうかを指定する
        ime_reconv_space  = False  # リージョンを選択した状態で Space キーを押下した際、「再変換」が働くか
                                   # どうかを指定する

    ## Windows 10 2004 以降の 新しい Microsoft IME の場合
    ## （新しい Microsoft IME には、確定取り消し（C-Backspace）の設定が無いようなので「再変換」のキー
    ## 　としている）
    if 0:
        ime_reconv_key = "W-Slash" # 「再変換」キー
        ime_cancel_key = "W-Slash" # 「確定の取り消し」キー
        ime_reconv_region = False  # 「再変換」の時にリージョンの選択が必要かどうかを指定する
        ime_reconv_space  = True   # リージョンを選択した状態で Space キーを押下した際、「再変換」が働くか
                                   # どうかを指定する

    ## Google日本語入力の「MS-IME」のキー設定の場合
    if 0:
        ime_reconv_key = "(28)"    # 「再変換」キー
        ime_cancel_key = "C-Back"  # 「確定の取り消し」キー
        ime_reconv_region = True   # 「再変換」の時にリージョンの選択が必要かどうかを指定する
        ime_reconv_space  = False  # リージョンを選択した状態で Space キーを押下した際、「再変換」が働くか
                                   # どうかを指定する

    ## Google日本語入力の「ことえり」のキー設定の場合
    if 0:
        ime_reconv_key = "C-S-r"   # 「再変換」キー
        ime_cancel_key = "C-Back"  # 「確定の取り消し」キー
        ime_reconv_region = True   # 「再変換」の時にリージョンの選択が必要かどうかを指定する
        ime_reconv_space  = False  # リージョンを選択した状態で Space キーを押下した際、「再変換」が働くか
                                   # どうかを指定する
    #---------------------------------------------------------------------------------------------------

    #---------------------------------------------------------------------------------------------------
    # Emacs日本語入力モードを利用する際に、IME のショートカットを置き換えるキーの組み合わせ
    # （置き換え先、置き換え元）を指定する
    # （if 文箇所は、Microsoft IME で「ことえり」のキーバインドを利用するための設定例です。
    # 　この設定は、Google日本語入力で「ことえり」のキー設定になっている場合には不要ですが、
    # 　設定を行っても問題はありません。）
    emacs_ime_mode_key = []
    if 1:
        emacs_ime_mode_key += [["C-i", "S-Left"],      # 文節を縮める
                               ["C-o", "S-Right"],     # 文節を伸ばす
                               ["C-j", "F6"],          # ひらがなに変換
                               ["C-k", "F7"],          # 全角カタカナに変換
                               ["C-l", "F9"],          # 全角英数に表示切替
                               ["C-Semicolon", "F8"]]  # 半角に変換

        if is_japanese_keyboard:
            emacs_ime_mode_key += [["C-Colon", "F10"]] # 半角英数に表示切替
        else:
            emacs_ime_mode_key += [["C-Quote", "F10"]] # 半角英数に表示切替
    #---------------------------------------------------------------------------------------------------

    # 数引数の指定に Ctrl+数字キーを使うかを指定する（True: 使う、False: 使わない）
    # （False に指定しても、C-u 数字キーで数引数を指定することができます）
    use_ctrl_digit_key_for_digit_argument = False

    # F1 から F12 を Alt+数字キー列として使うかを指定する（True: 使う、False: 使わない）
    use_alt_digit_key_for_f1_to_f12 = False

    # F13 から F24 を Alt-Shift+数字キー列として使うかを指定する（True: 使う、False: 使わない）
    use_alt_shift_digit_key_for_f13_to_f24 = False

    # 表示しているウィンドウの中で、一番最近までフォーカスがあったウィンドウに移動するキーを指定する
    other_window_key = "A-o"

    # クリップボードリストを起動するキーを指定する
    clipboardList_key = "A-y"

    # ランチャーリストを起動するキーを指定する
    lancherList_key = "A-l"

    # アクティブウィンドウを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # （内部で A-Tab による切り替えを行っているため、設定するキーは Altキーとの組み合わせとしてください）
    # （切り替え画面が起動した後は、A-b、A-f、A-p、A-n でウィンドウを切り替えられるように設定している他、
    #   Alt + 矢印キーでもウィンドウを切り替えることができます。また、A-g もしくは A-Esc で切り替え画面の
    #   終了（キャンセル）となり、Altキーを離すか A-Enter で切り替えるウィンドウの確定となります。）
    # （デフォルトキーは、["A-S-Tab", "A-Tab"]）
    window_switching_key = []
    # window_switching_key += [["A-p", "A-n"]]

    # アクティブウィンドウをディスプレイ間で移動するキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # （デフォルトキーは、["W-S-Left", "W-S-Right"]）
    window_movement_key_for_displays = []
    # window_movement_key_for_displays += [[None, "W-o"]]

    # ウィンドウを最小化、リストアするキーの組み合わせ（リストア、最小化 の順）を指定する（複数指定可）
    window_minimize_key = []
    # window_minimize_key += [["A-S-m", "A-m"]]

    # 仮想デスクトップを切り替えるキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # （仮想デスクトップを切り替えた際にフォーカスのあるウィンドウを適切に処理するため、設定するキーは
    # 　Winキーとの組み合わせとしてください）
    # （デフォルトキーは、["W-C-Left", "W-C-Right"]）
    desktop_switching_key = []
    # desktop_switching_key += [["W-b", "W-f"]]
    # desktop_switching_key += [["W-Left", "W-Right"]]

    # アクティブウィンドウを仮想デスクトップ間で移動するキーの組み合わせ（前、後 の順）を指定する（複数指定可）
    # （本機能を利用する場合は、Microsoft Store から SylphyHorn をインストールしてください）
    # （デフォルトキーは、["W-C-A-Left", "W-C-A-Right"] です。この設定は変更しないでください）
    window_movement_key_for_desktops = []
    # window_movement_key_for_desktops += [["W-p", "W-n"]]

    # IME の「単語登録」プログラムを起動するキーを指定する
    word_register_key = None
    # word_register_key = "C-CloseBracket"

    # IME の「単語登録」プログラムとそのパラメータを指定する（for MS-IME）
    word_register_name = r"C:\Windows\System32\IME\IMEJP\IMJPDCT.EXE"
    word_register_param = ""

    # IME の「単語登録」プログラムとそのパラメータを指定する（for Google日本語入力）
    # word_register_name = r"C:\Program Files (x86)\Google\Google Japanese Input\GoogleIMEJaTool.exe"
    # word_register_param = "--mode=word_register_dialog"

    # shell_command 関数で起動するアプリケーションソフトを指定する
    # （パスが通っていない場所にあるコマンドは、絶対パスで指定してください）
    command_name = r"cmd.exe"

    # コマンドのリピート回数の最大値を指定する
    repeat_max = 1024

    # Microsoft Excel のセル内で改行を選択可能かを指定する（True: 選択可、False: 選択不可）
    # （kill_line 関数の挙動を変えるための変数です。Microsoft Excel 2019 以降では True にして
    #   ください。）
    is_newline_selectable_in_Excel = False


    ####################################################################################################
    ## 基本設定
    ####################################################################################################

    # 変数を格納するクラスを定義する
    class Fakeymacs:
        pass

    fakeymacs = Fakeymacs()

    fakeymacs.last_window = None
    fakeymacs.ime_cancel = False

    def is_emacs_target(window):
        if window != fakeymacs.last_window:
            if window.getProcessName() in not_clipboard_target:
                # クリップボードの監視用のフックを無効にする
                keymap.clipboard_history.enableHook(False)
            else:
                # クリップボードの監視用のフックを有効にする
                keymap.clipboard_history.enableHook(True)

            fakeymacs.last_window = window
            fakeymacs.ime_cancel = False

        if is_task_switching_window(window):
            return False

        if is_list_window(window):
            return False

        if window.getClassName() in emacs_target_class:
            fakeymacs.keybind = "emacs"
            return True

        if window.getProcessName() in not_emacs_target:
            fakeymacs.keybind = "not_emacs"
            return False

        fakeymacs.keybind = "emacs"
        return True

    def is_ime_target(window):
        if window.getClassName() in emacs_target_class:
            return False

        if window.getProcessName() in ime_target:
            return True

        return False

    if use_emacs_ime_mode:
        keymap_emacs = keymap.defineWindowKeymap(check_func=lambda wnd: is_emacs_target(wnd) and not is_emacs_ime_mode(wnd))
        keymap_ime   = keymap.defineWindowKeymap(check_func=lambda wnd: is_ime_target(wnd)   and not is_emacs_ime_mode(wnd))
    else:
        keymap_emacs = keymap.defineWindowKeymap(check_func=is_emacs_target)
        keymap_ime   = keymap.defineWindowKeymap(check_func=is_ime_target)

    # mark がセットされると True になる
    fakeymacs.is_marked = False

    # リージョンを拡張する際に、順方向に拡張すると True、逆方向に拡張すると False になる
    fakeymacs.forward_direction = None

    # 検索が開始されると True になる
    fakeymacs.is_searching = False

    # キーボードマクロの play 中 は True になる
    fakeymacs.is_playing_kmacro = False

    # universal-argument コマンドが実行されると True になる
    fakeymacs.is_universal_argument = False

    # digit-argument コマンドが実行されると True になる
    fakeymacs.is_digit_argument = False

    # コマンドのリピート回数を設定する
    fakeymacs.repeat_counter = 1

    # undo のモードの時 True になる（redo のモードの時 False になる）
    fakeymacs.is_undo_mode = True

    # Ctl-xプレフィックスキーを構成するキーの仮想キーコードを設定する
    if ctl_x_prefix_key:
        keyCondition = keyhac_keymap.KeyCondition.fromString(ctl_x_prefix_key)

        if keyCondition.mod == MODKEY_CTRL:
            if side_of_ctrl_key == "L":
                ctl_x_prefix_vkey = [VK_LCONTROL, keyCondition.vk]
            else:
                ctl_x_prefix_vkey = [VK_RCONTROL, keyCondition.vk]

        elif keyCondition.mod == MODKEY_ALT:
            if side_of_alt_key == "L":
                ctl_x_prefix_vkey = [VK_LMENU, keyCondition.vk]
            else:
                ctl_x_prefix_vkey = [VK_RMENU, keyCondition.vk]
        else:
            print("Ctl-xプレフィックスキーのモディファイアキーは、Ctrl または Alt のいずれかから指定してください")

    ##################################################
    ## IME の操作
    ##################################################

    def enable_input_method():
        setImeStatus(1)

    def disable_input_method():
        setImeStatus(0)

    def toggle_input_method():
        setImeStatus(keymap.getWindow().getImeStatus() ^ 1)

    def setImeStatus(ime_status):
        if keymap.getWindow().getImeStatus() != ime_status:
            # IME を 切り替える
            # （ keymap.getWindow().setImeStatus(ime_status) を使わないのは、キーボードマクロの再生時に影響がでるため）
            self_insert_command("A-(25)")()

            if fakeymacs.is_playing_kmacro:
                delay(0.2)

        if not fakeymacs.is_playing_kmacro:
            if ime_status:
                message = "[あ]"
            else:
                message = "[A]"

            # IME の状態をバルーンヘルプで表示する
            keymap.popBalloon("ime_status", message, 500)

    def reconversion(reconv_key, cancel_key):
        def _func():
            if fakeymacs.ime_cancel:
                self_insert_command(cancel_key)()
                if use_emacs_ime_mode:
                    # バルーンメッセージのマークがずれて表示されないようにディレイを追加
                    delay()
                    enable_emacs_ime_mode()
            else:
                if ime_reconv_region:
                    if fakeymacs.forward_direction is not None:
                        self_insert_command(reconv_key)()
                        if use_emacs_ime_mode:
                            enable_emacs_ime_mode()
                else:
                    self_insert_command(reconv_key)()
                    if use_emacs_ime_mode:
                        enable_emacs_ime_mode()
        return _func

    ##################################################
    ## ファイル操作
    ##################################################

    def find_file():
        self_insert_command("C-o")()

    def save_buffer():
        self_insert_command("C-s")()

    def write_file():
        self_insert_command("A-f", "A-a")()

    def dired():
        keymap.ShellExecuteCommand(None, r"explorer.exe", "", "")()

    ##################################################
    ## カーソル移動
    ##################################################

    def backward_char():
        self_insert_command("Left")()

    def forward_char():
        self_insert_command("Right")()

    def backward_word():
        self_insert_command("C-Left")()

    def forward_word():
        self_insert_command("C-Right")()

    def previous_line():
        self_insert_command("Up")()

    def next_line():
        self_insert_command("Down")()

    def move_beginning_of_line():
        self_insert_command("Home")()

    def move_end_of_line():
        self_insert_command("End")()
        if (checkWindow("WINWORD.EXE", "_WwG") or      # Microsoft Word
            checkWindow("POWERPNT.EXE", "mdiClass") or # Microsoft PowerPoint
            (checkWindow("EXCEL.EXE", "EXCEL*") and    # Microsoft Excel
             is_newline_selectable_in_Excel)):
            if fakeymacs.is_marked:
                self_insert_command("Left")()

    def beginning_of_buffer():
        self_insert_command("C-Home")()

    def end_of_buffer():
        self_insert_command("C-End")()

    def scroll_up():
        self_insert_command("PageUp")()

    def scroll_down():
        self_insert_command("PageDown")()

    def recenter():
        if (checkWindow("sakura.exe", "EditorClient") or # Sakura Editor
            checkWindow("sakura.exe", "SakuraView166")): # Sakura Editor
            self_insert_command("C-h")()
        else:
            # recenter の機能をサポートしていないアプリケーションソフトについては、C-l を発行する。
            # これで chrome 等でのアドレスバーに移動する機能を実現できる。recenter の機能を呼ぶ
            # キーバインドを C-l と決め打ちしていることについては、とりあえず了承ください。
            self_insert_command("C-l")()

    ##################################################
    ## カット / コピー / 削除 / アンドゥ
    ##################################################

    def delete_backward_char():
        self_insert_command("Back")()

    def delete_char():
        self_insert_command("Delete")()

    def backward_kill_word(repeat=1):
        resetRegion()
        fakeymacs.is_marked = True

        def move_beginning_of_region():
            for i in range(repeat):
                backward_word()

        mark(move_beginning_of_region, False)()
        delay()
        kill_region()

    def kill_word(repeat=1):
        resetRegion()
        fakeymacs.is_marked = True

        def move_end_of_region():
            for i in range(repeat):
                forward_word()

        mark(move_end_of_region, True)()
        delay()
        kill_region()

    def kill_line(repeat=1):
        resetRegion()
        fakeymacs.is_marked = True

        if repeat == 1:
            mark(move_end_of_line, True)()
            delay()

            if (checkWindow("cmd.exe", "ConsoleWindowClass") or       # Cmd
                checkWindow("powershell.exe", "ConsoleWindowClass")): # PowerShell
                kill_region()

            elif checkWindow(None, "HM32CLIENT"): # Hidemaru Software
                kill_region()
                delay()
                if getClipboardText() == "":
                    self_insert_command("Delete")()
            else:
                # 改行を消せるようにするため Cut にはしていない
                copyRegion()
                self_insert_command("Delete")()
        else:
            def move_end_of_region():
                if checkWindow("WINWORD.EXE", "_WwG"): # Microsoft Word
                    for i in range(repeat):
                        next_line()
                    move_beginning_of_line()
                else:
                    for i in range(repeat - 1):
                        next_line()
                    move_end_of_line()
                    forward_char()

            mark(move_end_of_region, True)()
            delay()
            kill_region()

    def kill_region():
        # コマンドプロンプトには Cut に対応するショートカットがない。その対策。
        if checkWindow("cmd.exe", "ConsoleWindowClass"): # Cmd
            copyRegion()

            if fakeymacs.forward_direction is not None:
                if fakeymacs.forward_direction:
                    key = "Delete"
                else:
                    key = "Back"

                delay()
                for i in range(len(getClipboardText())):
                    self_insert_command(key)()
        else:
            cutRegion()

    def kill_ring_save():
        copyRegion()
        resetRegion()

    def yank():
        self_insert_command("C-v")()

    def undo():
        # redo（C-y）の機能を持っていないアプリケーションソフトは常に undo とする
        if checkWindow("notepad.exe", "Edit"): # NotePad
            self_insert_command("C-z")()
        else:
            if fakeymacs.is_undo_mode:
                self_insert_command("C-z")()
            else:
                self_insert_command("C-y")()

    def set_mark_command():
        if fakeymacs.is_marked or fakeymacs.forward_direction is not None:
            resetRegion()
            fakeymacs.is_marked = False
            fakeymacs.forward_direction = None
        else:
            fakeymacs.is_marked = True

    def mark_whole_buffer():
        if checkWindow("cmd.exe", "ConsoleWindowClass"): # Cmd
            # "Home", "C-a" では上手く動かない場合がある
            self_insert_command("Home", "S-End")()
            fakeymacs.forward_direction = True # 逆の設定にする

        elif checkWindow("powershell.exe", "ConsoleWindowClass"): # PowerShell
            self_insert_command("End", "S-Home")()
            fakeymacs.forward_direction = False

        elif (checkWindow("EXCEL.EXE", "EXCEL*") or # Microsoft Excel
              checkWindow(None, "Edit")):           # Edit クラス
            self_insert_command("C-End", "C-S-Home")()
            fakeymacs.forward_direction = False
        else:
            self_insert_command("C-Home", "C-a")()
            fakeymacs.forward_direction = False

        fakeymacs.is_marked = True

    def mark_page():
        mark_whole_buffer()

    ##################################################
    ## バッファ / ウィンドウ操作
    ##################################################

    def kill_buffer():
        self_insert_command("C-F4")()

    def switch_to_buffer():
        self_insert_command("C-Tab")()

    def other_window():
        window_list = getWindowList()
        for wnd in window_list[1:]:
            if not wnd.isMinimized():
                wnd.getLastActivePopup().setForeground()
                break

    ##################################################
    ## 文字列検索 / 置換
    ##################################################

    def isearch(direction):
        if checkWindow("powershell.exe", "ConsoleWindowClass"): # PowerShell
            self_insert_command({"backward":"C-r", "forward":"C-s"}[direction])()
        else:
            if fakeymacs.is_searching:
                if checkWindow("EXCEL.EXE", None): # Microsoft Excel
                    if checkWindow(None, "EDTBX"): # 検索ウィンドウ
                        self_insert_command({"backward":"A-S-f", "forward":"A-f"}[direction])()
                    else:
                        self_insert_command("C-f")()
                else:
                    self_insert_command({"backward":"S-F3", "forward":"F3"}[direction])()
            else:
                self_insert_command("C-f")()
                fakeymacs.is_searching = True

    def isearch_backward():
        isearch("backward")

    def isearch_forward():
        isearch("forward")

    def query_replace():
        if (checkWindow("sakura.exe", "EditorClient") or  # Sakura Editor
            checkWindow("sakura.exe", "SakuraView166") or # Sakura Editor
            checkWindow(None, "HM32CLIENT")):             # Hidemaru Software
            self_insert_command("C-r")()
        else:
            self_insert_command("C-h")()

    ##################################################
    ## キーボードマクロ
    ##################################################

    def kmacro_start_macro():
        disable_input_method()
        keymap.command_RecordStart()

    def kmacro_end_macro():
        keymap.command_RecordStop()
        # キーボードマクロの終了キー「Ctl-xプレフィックスキー + ")"」の Ctl-xプレフィックスキーがマクロに
        # 記録されてしまうのを対策する（キーボードマクロの終了キーの前提を「Ctl-xプレフィックスキー + ")"」
        # としていることについては、とりあえず了承ください。）
        if ctl_x_prefix_key and len(keymap.record_seq) >= 4:
            if (((keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[0], True) and
                  keymap.record_seq[len(keymap.record_seq) - 2] == (ctl_x_prefix_vkey[1], True)) or
                 (keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[1], True) and
                  keymap.record_seq[len(keymap.record_seq) - 2] == (ctl_x_prefix_vkey[0], True))) and
                keymap.record_seq[len(keymap.record_seq) - 3] == (ctl_x_prefix_vkey[1], False)):
                   keymap.record_seq.pop()
                   keymap.record_seq.pop()
                   keymap.record_seq.pop()
                   if keymap.record_seq[len(keymap.record_seq) - 1] == (ctl_x_prefix_vkey[0], False):
                       for i in range(len(keymap.record_seq) - 1, -1, -1):
                           if keymap.record_seq[i] == (ctl_x_prefix_vkey[0], False):
                               keymap.record_seq.pop()
                           else:
                               break
                   else:
                       # コントロール系の入力が連続して行われる場合があるための対処
                       keymap.record_seq.append((ctl_x_prefix_vkey[0], True))

    def kmacro_end_and_call_macro():
        def callKmacro():
            # キーボードマクロの最初が IME ON の場合、この delay が必要
            delay(0.2)
            fakeymacs.is_playing_kmacro = True
            disable_input_method()
            keymap.command_RecordPlay()
            fakeymacs.is_playing_kmacro = False

        keymap.delayedCall(callKmacro, 0)

    ##################################################
    ## その他
    ##################################################

    def space():
        self_insert_command("Space")()
        if use_emacs_ime_mode:
            if ime_reconv_space:
                if keymap.getWindow().getImeStatus():
                    if fakeymacs.forward_direction is not None:
                        enable_emacs_ime_mode()

    def newline():
        self_insert_command("Enter")()
        if not use_emacs_ime_mode:
            if keymap.getWindow().getImeStatus():
                fakeymacs.ime_cancel = True

    def newline_and_indent():
        self_insert_command("Enter", "Tab")()

    def open_line():
        self_insert_command("Enter", "Up", "End")()

    def indent_for_tab_command():
        self_insert_command("Tab")()

    def keyboard_quit():
        resetRegion()

        # Esc を発行して問題ないアプリケーションソフトには Esc を発行する
        if not (checkWindow("cmd.exe", "ConsoleWindowClass") or        # Cmd
                checkWindow("powershell.exe", "ConsoleWindowClass") or # PowerShell
                checkWindow("EXCEL.EXE", "EXCEL*") or                  # Microsoft Excel
                checkWindow("Evernote.exe", "WebViewHost")):           # Evernote
            self_insert_command("Esc")()

        keymap.command_RecordStop()

        if fakeymacs.is_undo_mode:
            fakeymacs.is_undo_mode = False
        else:
            fakeymacs.is_undo_mode = True

    def kill_emacs():
        # Excel のファイルを開いた直後一回目、kill_emacs が正常に動作しない。その対策。
        self_insert_command("D-Alt", "F4")()
        delay(0.1)
        self_insert_command("U-Alt")()

    def universal_argument():
        if fakeymacs.is_universal_argument:
            if fakeymacs.is_digit_argument:
                fakeymacs.is_universal_argument = False
            else:
                fakeymacs.repeat_counter *= 4
        else:
            fakeymacs.is_universal_argument = True
            fakeymacs.repeat_counter *= 4

    def digit_argument(number):
        if fakeymacs.is_digit_argument:
            fakeymacs.repeat_counter = fakeymacs.repeat_counter * 10 + number
        else:
            fakeymacs.repeat_counter = number
            fakeymacs.is_digit_argument = True

    def shell_command():
        def popCommandWindow(wnd, command):
            if wnd.isVisible() and not wnd.getOwner() and wnd.getProcessName() == command:
                popWindow(wnd)()
                fakeymacs.is_executing_command = True
                return False
            return True

        fakeymacs.is_executing_command = False
        Window.enum(popCommandWindow, os.path.basename(command_name))

        if not fakeymacs.is_executing_command:
            keymap.ShellExecuteCommand(None, command_name, "", "")()

    ##################################################
    ## 共通関数
    ##################################################

    def delay(sec=0.02):
        time.sleep(sec)

    def copyRegion():
        self_insert_command("C-c")()
        pushToClipboardList()

    def cutRegion():
        self_insert_command("C-x")()
        pushToClipboardList()

    def pushToClipboardList():
        # clipboard 監視の対象外とするアプリケーションソフトで copy / cut した場合でも
        # クリップボードの内容をクリップボードリストに登録する
        if keymap.getWindow().getProcessName() in not_clipboard_target:
            delay(0.1)
            clipboard_text = getClipboardText()
            if clipboard_text:
                keymap.clipboard_history._push(clipboard_text)

    def checkWindow(processName, className, window=None):
        if window is None:
            window = keymap.getWindow()
        return ((processName is None or fnmatch.fnmatch(window.getProcessName(), processName)) and
                (className is None or fnmatch.fnmatch(window.getClassName(), className)))

    def vkeys():
        vkeys = list(keyCondition.vk_str_table.keys())
        for vkey in [VK_MENU, VK_LMENU, VK_RMENU, VK_CONTROL, VK_LCONTROL, VK_RCONTROL, VK_SHIFT, VK_LSHIFT, VK_RSHIFT, VK_LWIN, VK_RWIN]:
            vkeys.remove(vkey)
        return vkeys

    def addSideOfModifierKey(key):
        key = re.sub(r'(^|-)(C-)', r'\1' + side_of_ctrl_key + r'\2', key)
        key = re.sub(r'(^|-)(A-)', r'\1' + side_of_alt_key  + r'\2', key)
        key = re.sub(r'(^|-)(W-)', r'\1' + side_of_win_key  + r'\2', key)
        return key

    def kbd(keys):
        if keys:
            keys_lists = [keys.split()]

            if keys_lists[0][0] == "Ctl-x":
                if ctl_x_prefix_key:
                    keys_lists[0][0] = ctl_x_prefix_key
                else:
                    keys_lists = []

            elif keys_lists[0][0].startswith("M-"):
                key = re.sub("^M-", "", keys_lists[0][0])
                keys_lists[0][0] = "A-" + key
                if  use_multi_stroke_open_bracket_as_esc:
                    keys_lists.append(["C-OpenBracket", key])
                if use_esc_as_meta:
                    keys_lists.append(["Esc", key])

            for keys_list in keys_lists:
                keys_list[0] = addSideOfModifierKey(keys_list[0])
        else:
            keys_lists = []

        return keys_lists

    def define_key(keymap, keys, command):
        for keys_list in kbd(keys):
            if len(keys_list) == 1:
                keymap[keys_list[0]] = command

                # Alt キーによるワンショットモディファイアを使った際にカーソルがメニューへ移動するのを解除する
                # https://www.haijin-boys.com/discussions/4583
                if re.match(keys_list[0], r"O-LAlt$", re.IGNORECASE):
                    keymap["D-LAlt"] = "D-LAlt", "(7)"

                if re.match(keys_list[0], r"O-RAlt$", re.IGNORECASE):
                    keymap["D-RAlt"] = "D-RAlt", "(7)"
            else:
                keymap[keys_list[0]][keys_list[1]] = command

    def self_insert_command(*keys):
        func = keymap.InputKeyCommand(*list(map(addSideOfModifierKey, keys)))
        def _func():
            func()
            fakeymacs.ime_cancel = False
        return _func

    def self_insert_command2(*keys):
        func = self_insert_command(*keys)
        def _func():
            func()
            if use_emacs_ime_mode:
                if keymap.getWindow().getImeStatus():
                    enable_emacs_ime_mode()
        return _func

    def digit(number):
        def _func():
            if fakeymacs.is_universal_argument:
                digit_argument(number)
            else:
                reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(str(number))))))()
        return _func

    def digit2(number):
        def _func():
            fakeymacs.is_universal_argument = True
            digit_argument(number)
        return _func

    def resetRegion():
        if fakeymacs.forward_direction is not None:

            if checkWindow(None, "Edit"): # Edit クラス
                # 選択されているリージョンのハイライトを解除するためにカーソルキーを発行する
                if fakeymacs.forward_direction:
                    self_insert_command("Right")()
                else:
                    self_insert_command("Left")()

            elif checkWindow("cmd.exe", "ConsoleWindowClass"): # Cmd
                # 選択されているリージョンのハイライトを解除するためにカーソルを移動する
                if fakeymacs.forward_direction:
                    self_insert_command("Right", "Left")()
                else:
                    self_insert_command("Left", "Right")()

            elif (checkWindow("powershell.exe", "ConsoleWindowClass") or # PowerShell
                  checkWindow("EXCEL.EXE", None)):                       # Microsoft Excel
                # 選択されているリージョンのハイライトを解除するためにカーソルを移動する
                if fakeymacs.forward_direction:
                    self_insert_command("Left", "Right")()
                else:
                    self_insert_command("Right", "Left")()
            else:
                # 選択されているリージョンのハイライトを解除するためにカーソルキーを発行する
                if fakeymacs.forward_direction:
                    self_insert_command("Right")()
                else:
                    self_insert_command("Left")()

    def mark(func, forward_direction):
        def _func():
            if fakeymacs.is_marked:
                # D-Shift だと、M-< や M-> 押下時に、D-Shift が解除されてしまう。その対策。
                self_insert_command("D-LShift", "D-RShift")()
                delay()
                func()
                self_insert_command("U-LShift", "U-RShift")()

                # fakeymacs.forward_direction が未設定の場合、設定する
                if fakeymacs.forward_direction is None:
                    fakeymacs.forward_direction = forward_direction
            else:
                fakeymacs.forward_direction = None
                func()
        return _func

    def mark2(func, forward_direction):
        def _func():
            if fakeymacs.is_marked:
                resetRegion()
                fakeymacs.forward_direction = None
            fakeymacs.is_marked = True
            mark(func, forward_direction)()
            fakeymacs.is_marked = False
        return _func

    def reset_mark(func):
        def _func():
            func()
            fakeymacs.is_marked = False
            fakeymacs.forward_direction = None
        return _func

    def reset_counter(func):
        def _func():
            func()
            fakeymacs.is_universal_argument = False
            fakeymacs.is_digit_argument = False
            fakeymacs.repeat_counter = 1
        return _func

    def reset_undo(func):
        def _func():
            func()
            fakeymacs.is_undo_mode = True
        return _func

    def reset_search(func):
        def _func():
            func()
            fakeymacs.is_searching = False
        return _func

    def repeat(func):
        def _func():
            if fakeymacs.repeat_counter > repeat_max:
                print("コマンドのリピート回数の最大値を超えています")
                repeat_counter = repeat_max
            else:
                repeat_counter = fakeymacs.repeat_counter

            # キーボードマクロの繰り返し実行を可能とするために初期化する
            fakeymacs.repeat_counter = 1

            for i in range(repeat_counter):
                func()
        return _func

    def repeat2(func):
        def _func():
            if fakeymacs.is_marked:
                fakeymacs.repeat_counter = 1
            repeat(func)()
        return _func

    def repeat3(func):
        def _func():
            if fakeymacs.repeat_counter > repeat_max:
                print("コマンドのリピート回数の最大値を超えています")
                repeat_counter = repeat_max
            else:
                repeat_counter = fakeymacs.repeat_counter

            func(repeat_counter)
        return _func

    ##################################################
    ## キーバインド
    ##################################################

    # キーバインドの定義に利用している表記の意味は次のとおりです。
    # ・S-    : Shiftキー
    # ・C-    : Ctrlキー
    # ・A-    : Altキー
    # ・M-    : Altキー と Esc、C-[ のプレフィックスキーを利用する３パターンを定義（emacs の Meta と同様）
    # ・W-    : Winキー
    # ・Ctl-x : ctl_x_prefix_key 変数で定義されているプレフィックスキーに置換え
    # ・(999) : 仮想キーコード指定

    # https://github.com/crftwr/keyhac/blob/master/keyhac_keymap.py
    # https://github.com/crftwr/pyauto/blob/master/pyauto_const.py
    # http://www.yoshidastyle.net/2007/10/windowswin32api.html
    # http://www.azaelia.net/factory/vk.html
    # http://www3.airnet.ne.jp/saka/hardware/keyboard/109scode.html

    ## マルチストロークキーの設定
    define_key(keymap_emacs, "Ctl-x",         keymap.defineMultiStrokeKeymap(ctl_x_prefix_key))
    define_key(keymap_emacs, "C-q",           keymap.defineMultiStrokeKeymap("C-q"))
    if  use_multi_stroke_open_bracket_as_esc:
        define_key(keymap_emacs, "C-OpenBracket", keymap.defineMultiStrokeKeymap("C-OpenBracket"))
    if use_esc_as_meta:
        define_key(keymap_emacs, "Esc", keymap.defineMultiStrokeKeymap("Esc"))

    ## 数字キーの設定
    # for key in range(10):
    #     s_key = str(key)
    #     define_key(keymap_emacs, s_key, digit(key))
    #     if use_ctrl_digit_key_for_digit_argument:
    #         define_key(keymap_emacs, "C-" + s_key, digit2(key))
    #     define_key(keymap_emacs, "M-" + s_key, digit2(key))
    #     define_key(keymap_emacs, "S-" + s_key, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_key))))))
    #     define_key(keymap_ime,          s_key, self_insert_command2(       s_key))
    #     define_key(keymap_ime,   "S-" + s_key, self_insert_command2("S-" + s_key))

    ## アルファベットキーの設定
    # for vkey in range(VK_A, VK_Z + 1):
    #     s_vkey = "(" + str(vkey) + ")"
    #     define_key(keymap_emacs,        s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(       s_vkey))))))
    #     define_key(keymap_emacs, "S-" + s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_vkey))))))
    #     define_key(keymap_ime,          s_vkey, self_insert_command2(       s_vkey))
    #     define_key(keymap_ime,   "S-" + s_vkey, self_insert_command2("S-" + s_vkey))

    ## 特殊文字キーの設定
    # define_key(keymap_emacs, "Space"  , reset_undo(reset_counter(reset_mark(repeat(space)))))
    # define_key(keymap_emacs, "S-Space", reset_undo(reset_counter(reset_mark(repeat(self_insert_command("S-Space"))))))

    # for vkey in [VK_OEM_MINUS, VK_OEM_PLUS, VK_OEM_COMMA, VK_OEM_PERIOD, VK_OEM_1, VK_OEM_2, VK_OEM_3, VK_OEM_4, VK_OEM_5, VK_OEM_6, VK_OEM_7, VK_OEM_102]:
    #     s_vkey = "(" + str(vkey) + ")"
    #     define_key(keymap_emacs,        s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(       s_vkey))))))
    #     define_key(keymap_emacs, "S-" + s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2("S-" + s_vkey))))))
    #     define_key(keymap_ime,          s_vkey, self_insert_command2(       s_vkey))
    #     define_key(keymap_ime,   "S-" + s_vkey, self_insert_command2("S-" + s_vkey))

    ## 10key の特殊文字キーの設定
    # for vkey in [VK_MULTIPLY, VK_ADD, VK_SUBTRACT, VK_DECIMAL, VK_DIVIDE]:
    #     s_vkey = "(" + str(vkey) + ")"
    #     define_key(keymap_emacs, s_vkey, reset_undo(reset_counter(reset_mark(repeat(self_insert_command2(s_vkey))))))
    #     define_key(keymap_ime,   s_vkey, self_insert_command2(s_vkey))

    ## quoted-insertキーの設定
    for vkey in vkeys():
        s_vkey = "(" + str(vkey) + ")"
        define_key(keymap_emacs, "C-q "     + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command(         s_vkey))))))
        define_key(keymap_emacs, "C-q S-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("S-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q C-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q C-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-S-" + s_vkey))))))
        define_key(keymap_emacs, "C-q A-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q A-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-S-" + s_vkey))))))
        define_key(keymap_emacs, "C-q W-"   + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("W-"   + s_vkey))))))
        define_key(keymap_emacs, "C-q W-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("W-S-" + s_vkey))))))

    ## C-S-[a-z] -> C-[a-z]、A-S-[a-z] -> A-[a-z] の置き換え設定（Emacsシフトモードの設定）
    if use_emacs_shift_mode:
        for vkey in range(VK_A, VK_Z + 1):
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_emacs, "C-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("C-" + s_vkey))))))
            define_key(keymap_emacs, "A-S-" + s_vkey, reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("A-" + s_vkey))))))
            define_key(keymap_ime,   "C-S-" + s_vkey, self_insert_command("C-" + s_vkey))
            define_key(keymap_ime,   "A-S-" + s_vkey, self_insert_command("A-" + s_vkey))

    ## Escキーの設定
    if use_multi_stroke_open_bracket_as_esc:
        define_key(keymap_emacs, "C-OpenBracket C-OpenBracket", reset_undo(reset_counter(self_insert_command("Esc"))))
    else:
        define_key(keymap_emacs, "C-OpenBracket", reset_undo(reset_counter(self_insert_command("Esc"))))
    if use_esc_as_meta:
        define_key(keymap_emacs, "Esc Esc", reset_undo(reset_counter(self_insert_command("Esc"))))
    else:
        define_key(keymap_emacs, "Esc", reset_undo(reset_counter(self_insert_command("Esc"))))

    ## universal-argumentキーの設定
    # define_key(keymap_emacs, "C-u", universal_argument)

    ## 「IME の切り替え」のキー設定
    define_key(keymap_emacs, "(243)",  toggle_input_method)
    define_key(keymap_emacs, "(244)",  toggle_input_method)
    define_key(keymap_emacs, "A-(25)", toggle_input_method)

    define_key(keymap_ime,   "(243)",  toggle_input_method)
    define_key(keymap_ime,   "(244)",  toggle_input_method)
    define_key(keymap_ime,   "A-(25)", toggle_input_method)

    ## 「ファイル操作」のキー設定
    define_key(keymap_emacs, "Ctl-x C-f", reset_search(reset_undo(reset_counter(reset_mark(find_file)))))
    define_key(keymap_emacs, "Ctl-x C-s", reset_search(reset_undo(reset_counter(reset_mark(save_buffer)))))
    define_key(keymap_emacs, "Ctl-x C-w", reset_search(reset_undo(reset_counter(reset_mark(write_file)))))
    define_key(keymap_emacs, "Ctl-x d",   reset_search(reset_undo(reset_counter(reset_mark(dired)))))

    ## 「カーソル移動」のキー設定
    define_key(keymap_emacs, "C-b",        reset_search(reset_undo(reset_counter(mark(repeat(backward_char), False)))))
    define_key(keymap_emacs, "C-f",        reset_search(reset_undo(reset_counter(mark(repeat(forward_char), True)))))
    define_key(keymap_emacs, "M-b",        reset_search(reset_undo(reset_counter(mark(repeat(backward_word), False)))))
    define_key(keymap_emacs, "M-f",        reset_search(reset_undo(reset_counter(mark(repeat(forward_word), True)))))
    define_key(keymap_emacs, "C-p",        reset_search(reset_undo(reset_counter(mark(repeat(previous_line), False)))))
    define_key(keymap_emacs, "C-n",        reset_search(reset_undo(reset_counter(mark(repeat(next_line), True)))))
    define_key(keymap_emacs, "C-a",        reset_search(reset_undo(reset_counter(mark(move_beginning_of_line, False)))))
    define_key(keymap_emacs, "C-e",        reset_search(reset_undo(reset_counter(mark(move_end_of_line, True)))))
    define_key(keymap_emacs, "M-S-Comma",  reset_search(reset_undo(reset_counter(mark(beginning_of_buffer, False)))))
    define_key(keymap_emacs, "M-S-Period", reset_search(reset_undo(reset_counter(mark(end_of_buffer, True)))))
    # define_key(keymap_emacs, "C-l",        reset_search(reset_undo(reset_counter(recenter))))

    # if not use_emacs_shift_mode:
    #     define_key(keymap_emacs, "C-S-b", reset_search(reset_undo(reset_counter(mark2(repeat(backward_char), False)))))
    #     define_key(keymap_emacs, "C-S-f", reset_search(reset_undo(reset_counter(mark2(repeat(forward_char), True)))))
    #     define_key(keymap_emacs, "M-S-b", reset_search(reset_undo(reset_counter(mark2(repeat(backward_word), False)))))
    #     define_key(keymap_emacs, "M-S-f", reset_search(reset_undo(reset_counter(mark2(repeat(forward_word), True)))))
    #     define_key(keymap_emacs, "C-S-p", reset_search(reset_undo(reset_counter(mark2(repeat(previous_line), False)))))
    #     define_key(keymap_emacs, "C-S-n", reset_search(reset_undo(reset_counter(mark2(repeat(next_line), True)))))
    #     define_key(keymap_emacs, "C-S-a", reset_search(reset_undo(reset_counter(mark2(move_beginning_of_line, False)))))
    #     define_key(keymap_emacs, "C-S-e", reset_search(reset_undo(reset_counter(mark2(move_end_of_line, True)))))

    # define_key(keymap_emacs, "Left",     reset_search(reset_undo(reset_counter(mark(repeat(backward_char), False)))))
    # define_key(keymap_emacs, "Right",    reset_search(reset_undo(reset_counter(mark(repeat(forward_char), True)))))
    # define_key(keymap_emacs, "C-Left",   reset_search(reset_undo(reset_counter(mark(repeat(backward_word), False)))))
    # define_key(keymap_emacs, "C-Right",  reset_search(reset_undo(reset_counter(mark(repeat(forward_word), True)))))
    # define_key(keymap_emacs, "Up",       reset_search(reset_undo(reset_counter(mark(repeat(previous_line), False)))))
    # define_key(keymap_emacs, "Down",     reset_search(reset_undo(reset_counter(mark(repeat(next_line), True)))))
    # define_key(keymap_emacs, "Home",     reset_search(reset_undo(reset_counter(mark(move_beginning_of_line, False)))))
    # define_key(keymap_emacs, "End",      reset_search(reset_undo(reset_counter(mark(move_end_of_line, True)))))
    # define_key(keymap_emacs, "C-Home",   reset_search(reset_undo(reset_counter(mark(beginning_of_buffer, False)))))
    # define_key(keymap_emacs, "C-End",    reset_search(reset_undo(reset_counter(mark(end_of_buffer, True)))))
    # define_key(keymap_emacs, "PageUP",   reset_search(reset_undo(reset_counter(mark(scroll_up, False)))))
    # define_key(keymap_emacs, "PageDown", reset_search(reset_undo(reset_counter(mark(scroll_down, True)))))

    # define_key(keymap_emacs, "S-Left",     reset_search(reset_undo(reset_counter(mark2(repeat(backward_char), False)))))
    # define_key(keymap_emacs, "S-Right",    reset_search(reset_undo(reset_counter(mark2(repeat(forward_char), True)))))
    # define_key(keymap_emacs, "C-S-Left",   reset_search(reset_undo(reset_counter(mark2(repeat(backward_word), False)))))
    # define_key(keymap_emacs, "C-S-Right",  reset_search(reset_undo(reset_counter(mark2(repeat(forward_word), True)))))
    # define_key(keymap_emacs, "S-Up",       reset_search(reset_undo(reset_counter(mark2(repeat(previous_line), False)))))
    # define_key(keymap_emacs, "S-Down",     reset_search(reset_undo(reset_counter(mark2(repeat(next_line), True)))))
    # define_key(keymap_emacs, "S-Home",     reset_search(reset_undo(reset_counter(mark2(move_beginning_of_line, False)))))
    # define_key(keymap_emacs, "S-End",      reset_search(reset_undo(reset_counter(mark2(move_end_of_line, True)))))
    # define_key(keymap_emacs, "C-S-Home",   reset_search(reset_undo(reset_counter(mark2(beginning_of_buffer, False)))))
    # define_key(keymap_emacs, "C-S-End",    reset_search(reset_undo(reset_counter(mark2(end_of_buffer, True)))))
    # define_key(keymap_emacs, "S-PageUP",   reset_search(reset_undo(reset_counter(mark2(scroll_up, False)))))
    # define_key(keymap_emacs, "S-PageDown", reset_search(reset_undo(reset_counter(mark2(scroll_down, True)))))

    ## 「カット / コピー / 削除 / アンドゥ」のキー設定
    define_key(keymap_emacs, "C-h",      reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_backward_char))))))
    define_key(keymap_emacs, "C-d",      reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_char))))))
    define_key(keymap_emacs, "M-Delete", reset_search(reset_undo(reset_counter(reset_mark(repeat3(backward_kill_word))))))
    define_key(keymap_emacs, "M-d",      reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_word))))))
    define_key(keymap_emacs, "C-k",      reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_line))))))
    define_key(keymap_emacs, "C-w",      reset_search(reset_undo(reset_counter(reset_mark(kill_region)))))
    define_key(keymap_emacs, "M-w",      reset_search(reset_undo(reset_counter(reset_mark(kill_ring_save)))))
    define_key(keymap_emacs, "C-y",      reset_search(reset_undo(reset_counter(reset_mark(repeat(yank))))))
    define_key(keymap_emacs, "C-Slash",  reset_search(reset_counter(reset_mark(undo))))
    define_key(keymap_emacs, "Ctl-x u",  reset_search(reset_counter(reset_mark(undo))))

    # define_key(keymap_emacs, "Back",     reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_backward_char))))))
    define_key(keymap_emacs, "Delete",   reset_search(reset_undo(reset_counter(reset_mark(repeat2(delete_char))))))
    define_key(keymap_emacs, "C-Back",   reset_search(reset_undo(reset_counter(reset_mark(repeat3(backward_kill_word))))))
    define_key(keymap_emacs, "C-Delete", reset_search(reset_undo(reset_counter(reset_mark(repeat3(kill_word))))))
    define_key(keymap_emacs, "C-c",      reset_search(reset_undo(reset_counter(reset_mark(kill_ring_save)))))
    # define_key(keymap_emacs, "C-v",      reset_search(reset_undo(reset_counter(reset_mark(repeat(yank)))))) # scroll_key の設定で上書きされない場合
    # define_key(keymap_emacs, "C-z",      reset_search(reset_counter(reset_mark(undo))))

    # C-Underscore を機能させるための設定
    if is_japanese_keyboard:
        define_key(keymap_emacs, "C-S-BackSlash", reset_search(reset_undo(reset_counter(reset_mark(undo)))))
    else:
        define_key(keymap_emacs, "C-S-Minus", reset_search(reset_undo(reset_counter(reset_mark(undo)))))

    if is_japanese_keyboard:
        # C-Atmark だとうまく動かない方が居るようなので C-(192) としている
        # （http://bhby39.blogspot.jp/2015/02/windows-emacs.html）
        define_key(keymap_emacs, "C-(192)", reset_search(reset_undo(reset_counter(set_mark_command))))
    else:
        # C-S-2 は有効とならないが、一応設定は行っておく（C-S-3 などは有効となる。なぜだろう？）
        define_key(keymap_emacs, "C-S-2", reset_search(reset_undo(reset_counter(set_mark_command))))

    define_key(keymap_emacs, "C-Space",   reset_search(reset_undo(reset_counter(set_mark_command))))
    define_key(keymap_emacs, "Ctl-x h",   reset_search(reset_undo(reset_counter(mark_whole_buffer))))
    define_key(keymap_emacs, "M-a",       reset_search(reset_undo(reset_counter(mark_whole_buffer))))
    define_key(keymap_emacs, "Ctl-x C-p", reset_search(reset_undo(reset_counter(mark_page))))

    ## 「バッファ / ウィンドウ操作」のキー設定
    define_key(keymap_emacs, "Ctl-x k", reset_search(reset_undo(reset_counter(reset_mark(kill_buffer)))))
    define_key(keymap_emacs, "Ctl-x b", reset_search(reset_undo(reset_counter(reset_mark(switch_to_buffer)))))
    define_key(keymap_emacs, "Ctl-x o", reset_search(reset_undo(reset_counter(reset_mark(other_window)))))
    define_key(keymap_emacs, "M-k",     reset_search(reset_undo(reset_counter(reset_mark(kill_buffer)))))

    ## 「文字列検索 / 置換」のキー設定
    define_key(keymap_emacs, "C-r",   reset_undo(reset_counter(reset_mark(isearch_backward))))
    define_key(keymap_emacs, "C-s",   reset_undo(reset_counter(reset_mark(isearch_forward))))
    define_key(keymap_emacs, "M-S-5", reset_search(reset_undo(reset_counter(reset_mark(query_replace)))))

    ## 「キーボードマクロ」のキー設定
    if is_japanese_keyboard:
        define_key(keymap_emacs, "Ctl-x S-8", kmacro_start_macro)
        define_key(keymap_emacs, "Ctl-x S-9", kmacro_end_macro)
    else:
        define_key(keymap_emacs, "Ctl-x S-9", kmacro_start_macro)
        define_key(keymap_emacs, "Ctl-x S-0", kmacro_end_macro)

    define_key(keymap_emacs, "Ctl-x e", reset_search(reset_undo(reset_counter(repeat(kmacro_end_and_call_macro)))))

    ## 「その他」のキー設定
    define_key(keymap_emacs, "Enter",     reset_undo(reset_counter(reset_mark(repeat(newline)))))
    define_key(keymap_emacs, "C-m",       reset_undo(reset_counter(reset_mark(repeat(newline)))))
    # define_key(keymap_emacs, "C-j",       reset_undo(reset_counter(reset_mark(newline_and_indent))))
    define_key(keymap_emacs, "C-o",       reset_undo(reset_counter(reset_mark(repeat(open_line)))))
    define_key(keymap_emacs, "Tab",       reset_undo(reset_counter(reset_mark(repeat(indent_for_tab_command)))))
    define_key(keymap_emacs, "C-g",       reset_search(reset_counter(reset_mark(keyboard_quit))))
    define_key(keymap_emacs, "Ctl-x C-c", reset_search(reset_undo(reset_counter(reset_mark(kill_emacs)))))
    define_key(keymap_emacs, "M-S-1",     reset_search(reset_undo(reset_counter(reset_mark(shell_command)))))

    if use_ctrl_i_as_tab:
        define_key(keymap_emacs, "C-i", reset_undo(reset_counter(reset_mark(repeat(indent_for_tab_command)))))

    ## 「スクロール」のキー設定
    if scroll_key:
        define_key(keymap_emacs, scroll_key[0], reset_search(reset_undo(reset_counter(mark(scroll_up, False)))))
        define_key(keymap_emacs, scroll_key[1], reset_search(reset_undo(reset_counter(mark(scroll_up, False)))))
        define_key(keymap_emacs, scroll_key[2], reset_search(reset_undo(reset_counter(mark(scroll_down, True)))))

    ## 「カット」のキー設定
    if ctl_x_prefix_key != "C-x":
        define_key(keymap_emacs, "C-x", reset_search(reset_undo(reset_counter(reset_mark(kill_region)))))

    ## 「IME の切り替え」のキー設定
    if toggle_input_method_key:
        for key in toggle_input_method_key:
            define_key(keymap_emacs, key, toggle_input_method)
            define_key(keymap_ime,   key, toggle_input_method)

    ## 「IME の切り替え」のキー設定
    if set_input_method_key:
        for disable_key, enable_key in set_input_method_key:
            if disable_key:
                define_key(keymap_emacs, disable_key, disable_input_method)
                define_key(keymap_ime,   disable_key, disable_input_method)
            if enable_key:
                define_key(keymap_emacs, enable_key, enable_input_method)
                define_key(keymap_ime,   enable_key, enable_input_method)

    ## 「再変換」、「確定取り消し」のキー設定
    if reconversion_key:
        for key in reconversion_key:
            define_key(keymap_emacs, key, reset_undo(reset_counter(reset_mark(reconversion(ime_reconv_key, ime_cancel_key)))))

    ####################################################################################################
    ## Visual Studioのキーバインド
    ####################################################################################################
    keymap_devenv = keymap.defineWindowKeymap( exe_name="devenv.exe")

    keymap_devenv[ "C-h" ] = "Back"

    ####################################################################################################
    ## Emacs日本語入力モードの設定
    ####################################################################################################
    if use_emacs_ime_mode:

        def is_emacs_ime_mode(window):
            if fakeymacs.ei_last_window == window:
                return True
            else:
                fakeymacs.ei_last_window = None
                return False

        def is_emacs_ime_mode2(window):
            if is_emacs_ime_mode(window):
                ei_popBalloon(1)
                return True
            else:
                ei_popBalloon(0)
                return False

        keymap_ei = keymap.defineWindowKeymap(check_func=is_emacs_ime_mode2)

        # Emacs日本語入力モードが開始されたときのウィンドウオブジェクトを格納する変数を初期化する
        fakeymacs.ei_last_window = None

        ##################################################
        ## Emacs日本語入力モード の切り替え
        ##################################################

        def enable_emacs_ime_mode():
            fakeymacs.ei_last_window = keymap.getWindow()
            fakeymacs.ei_last_func = None
            ei_updateKeymap()

        def disable_emacs_ime_mode():
            fakeymacs.ei_last_window = None
            ei_updateKeymap()

        ##################################################
        ## IME の切り替え（Emacs日本語入力モード用）
        ##################################################

        def ei_enable_input_method():
            # IME の状態のバルーンヘルプを表示するために敢えてコールする
            enable_input_method()

        def ei_disable_input_method():
            disable_emacs_ime_mode()
            disable_input_method()

        def ei_enable_input_method2(key, ei_keymap):
            keyConditon = keyhac_keymap.KeyCondition.fromString(key)
            if keyConditon in ei_keymap:
                func = keymap_ei[key]
            else:
                func = ei_record_func(self_insert_command(key))

            def _func():
                if fakeymacs.ei_last_func == delete_backward_char:
                    ei_enable_input_method()
                elif key.startswith("O-"):
                    ei_record_func(self_insert_command("(28)")) # [変換]キー 発行
                else:
                    func()
            return _func

        def ei_disable_input_method2(key, ei_keymap):
            keyConditon = keyhac_keymap.KeyCondition.fromString(key)
            if keyConditon in ei_keymap:
                func = keymap_ei[key]
            else:
                func = ei_record_func(self_insert_command(key))

            def _func():
                if fakeymacs.ei_last_func == delete_backward_char:
                    ei_disable_input_method()
                elif key.startswith("O-"):
                    ei_record_func(self_insert_command("(29)")) # [無変換]キー 発行
                else:
                    func()
            return _func

        ##################################################
        ## その他（Emacs日本語入力モード用）
        ##################################################

        def ei_esc():
            self_insert_command("Esc")()

        def ei_newline():
            self_insert_command("Enter")()
            fakeymacs.ime_cancel = True
            disable_emacs_ime_mode()

        def ei_keyboard_quit():
            self_insert_command("Esc")()
            disable_emacs_ime_mode()

        ##################################################
        ## 共通関数（Emacs日本語入力モード用）
        ##################################################

        def ei_record_func(func):
            def _func():
                func()
                fakeymacs.ei_last_func = func
            return _func

        def ei_popBalloon(ime_mode_status):
            if not fakeymacs.is_playing_kmacro:
                if emacs_ime_mode_balloon_message:
                    if ime_mode_status:
                        keymap.popBalloon("emacs_ime_mode", emacs_ime_mode_balloon_message)
                    else:
                        keymap.closeBalloon("emacs_ime_mode")

        def ei_updateKeymap():
            if fakeymacs.is_playing_kmacro:
                keymap.updateKeymap()
            else:
                keymap.delayedCall(keymap.updateKeymap, 0)

        ##################################################
        ## キーバインド（Emacs日本語入力モード用）
        ##################################################

        ## 全てキーパターンの設定（ei_record_func 関数を通すための設定）
        for vkey in vkeys():
            s_vkey = "(" + str(vkey) + ")"
            define_key(keymap_ei,          s_vkey, ei_record_func(self_insert_command(         s_vkey)))
            define_key(keymap_ei, "S-"   + s_vkey, ei_record_func(self_insert_command("S-"   + s_vkey)))
            define_key(keymap_ei, "C-"   + s_vkey, ei_record_func(self_insert_command("C-"   + s_vkey)))
            define_key(keymap_ei, "C-S-" + s_vkey, ei_record_func(self_insert_command("C-S-" + s_vkey)))
            define_key(keymap_ei, "A-"   + s_vkey, ei_record_func(self_insert_command("A-"   + s_vkey)))
            define_key(keymap_ei, "A-S-" + s_vkey, ei_record_func(self_insert_command("A-S-" + s_vkey)))

        ## C-S-[a-z] -> C-[a-z]、A-S-[a-z] -> A-[a-z] の置き換え設定（Emacsシフトモードの設定）
        if use_emacs_shift_mode:
            for vkey in range(VK_A, VK_Z + 1):
                s_vkey = "(" + str(vkey) + ")"
                define_key(keymap_ei, "C-S-" + s_vkey, ei_record_func(self_insert_command("C-" + s_vkey)))
                define_key(keymap_ei, "A-S-" + s_vkey, ei_record_func(self_insert_command("A-" + s_vkey)))

        ## 「IME の切り替え」のキー設定
        define_key(keymap_ei, "(243)",  ei_disable_input_method)
        define_key(keymap_ei, "(244)",  ei_disable_input_method)
        define_key(keymap_ei, "A-(25)", ei_disable_input_method)

        ## Escキーの設定
        define_key(keymap_ei, "Esc",           ei_record_func(ei_esc))
        define_key(keymap_ei, "C-OpenBracket", ei_record_func(ei_esc))

        ## 「カーソル移動」のキー設定
        define_key(keymap_ei, "C-b", ei_record_func(backward_char))
        define_key(keymap_ei, "C-f", ei_record_func(forward_char))
        define_key(keymap_ei, "C-p", ei_record_func(previous_line))
        define_key(keymap_ei, "C-n", ei_record_func(next_line))
        define_key(keymap_ei, "C-a", ei_record_func(move_beginning_of_line))
        define_key(keymap_ei, "C-e", ei_record_func(move_end_of_line))

        define_key(keymap_ei, "Left",     ei_record_func(backward_char))
        define_key(keymap_ei, "Right",    ei_record_func(forward_char))
        define_key(keymap_ei, "Up",       ei_record_func(previous_line))
        define_key(keymap_ei, "Down",     ei_record_func(next_line))
        define_key(keymap_ei, "Home",     ei_record_func(move_beginning_of_line))
        define_key(keymap_ei, "End",      ei_record_func(move_end_of_line))
        define_key(keymap_ei, "PageUP",   ei_record_func(scroll_up))
        define_key(keymap_ei, "PageDown", ei_record_func(scroll_down))

        ## 「カット / コピー / 削除 / アンドゥ」のキー設定
        define_key(keymap_ei, "Back",   ei_record_func(delete_backward_char))
        define_key(keymap_ei, "C-h",    ei_record_func(delete_backward_char))
        define_key(keymap_ei, "Delete", ei_record_func(delete_char))
        define_key(keymap_ei, "C-d",    ei_record_func(delete_char))

        ## 「その他」のキー設定
        define_key(keymap_ei, "Enter", ei_newline)
        define_key(keymap_ei, "C-m",   ei_newline)
        define_key(keymap_ei, "Tab",   ei_record_func(indent_for_tab_command))
        define_key(keymap_ei, "C-g",   ei_keyboard_quit)

        ## 「スクロール」のキー設定
        if scroll_key:
            if scroll_key[0]:
                define_key(keymap_ei, scroll_key[0].replace("M-", "A-"), ei_record_func(scroll_up))
            if scroll_key[1]:
                define_key(keymap_ei, scroll_key[1].replace("M-", "A-"), ei_record_func(scroll_down))
            if scroll_key[2]:
                define_key(keymap_ei, scroll_key[2].replace("M-", "A-"), ei_record_func(scroll_down))

        # 「IME のショートカットの置き換え」のキー設定
        if emacs_ime_mode_key:
            for replace_key, original_key in emacs_ime_mode_key:
                define_key(keymap_ei, replace_key, ei_record_func(self_insert_command(original_key)))

        # この時点の keymap_ie のキーマップをコピーする
        ei_keymap = copy.copy(keymap_ei.keymap)

        ## 「IME の切り替え」のキー設定
        if toggle_input_method_key:
            for key in toggle_input_method_key:
                define_key(keymap_ei, key, ei_disable_input_method2(key, ei_keymap))

        ## 「IME の切り替え」のキー設定
        if set_input_method_key:
            for disable_key, enable_key in set_input_method_key:
                if disable_key:
                    define_key(keymap_ei, disable_key, ei_disable_input_method2(disable_key, ei_keymap))
                if enable_key:
                    define_key(keymap_ei, enable_key, ei_enable_input_method2(enable_key, ei_keymap))


    ####################################################################################################
    ## ファンクションの設定
    ####################################################################################################

    keymap_global = keymap.defineWindowKeymap()

    ##################################################
    ## ワンショットモディファイア
    ##################################################

    keymap.replaceKey( "Enter", "LCtrl" )
    keymap_global["O-LCtrl"] = "Enter"

    ##################################################
    ## キーバインド（ファンクション用）
    ##################################################

    ## Alt+数字キー列の設定
    if use_alt_digit_key_for_f1_to_f12:
        for i in range(10):
            define_key(keymap_global, "A-" + str(i + 1), self_insert_command("(" + str(VK_F1 + i) + ")"))

        define_key(keymap_global, "A-0", self_insert_command("(" + str(VK_F10) + ")"))

        if is_japanese_keyboard:
            define_key(keymap_global, "A-Minus", self_insert_command("(" + str(VK_F11) + ")"))
            define_key(keymap_global, "A-Caret", self_insert_command("(" + str(VK_F12) + ")"))
        else:
            define_key(keymap_global, "A-Minus", self_insert_command("(" + str(VK_F11) + ")"))
            define_key(keymap_global, "A-Plus",  self_insert_command("(" + str(VK_F12) + ")"))

    ## Alt+Shift+数字キー列の設定
    if use_alt_shift_digit_key_for_f13_to_f24:
        for i in range(10):
            define_key(keymap_global, "A-S-" + str(i + 1), self_insert_command("(" + str(VK_F1 + 12 + i) + ")"))

        define_key(keymap_global, "A-S-0", self_insert_command("(" + str(VK_F10 + 12) + ")"))

        if is_japanese_keyboard:
            define_key(keymap_global, "A-S-Minus", self_insert_command("(" + str(VK_F11 + 12) + ")"))
            define_key(keymap_global, "A-S-Caret", self_insert_command("(" + str(VK_F12 + 12) + ")"))
        else:
            define_key(keymap_global, "A-S-Minus", self_insert_command("(" + str(VK_F11 + 12) + ")"))
            define_key(keymap_global, "A-S-Plus",  self_insert_command("(" + str(VK_F12 + 12) + ")"))


    ####################################################################################################
    ## デスクトップの設定
    ####################################################################################################

    ##################################################
    ## ウィンドウ操作（デスクトップ用）
    ##################################################

    def popWindow(wnd):
        def _func():
            try:
                if wnd.isMinimized():
                    wnd.restore()
                wnd.getLastActivePopup().setForeground()
            except:
                print("選択したウィンドウは存在しませんでした")
        return _func

    def getWindowList():
        def makeWindowList(wnd, arg):
            if wnd.isVisible() and not wnd.getOwner():

                class_name = wnd.getClassName()
                title = wnd.getText()

                if class_name == "Emacs" or title != "":

                    # 操作の対象としたくないアプリケーションソフトの“クラス名称”を、re.match 関数
                    # （先頭からのマッチ）の正規表現に「|」を使って繋げて指定してください。
                    # （完全マッチとするためには $ の指定が必要です。）
                    if not re.match(r"Progman$", class_name):

                        process_name = wnd.getProcessName()

                        # 操作の対象としたくないアプリケーションソフトの“プロセス名称”を、re.match 関数
                        # （先頭からのマッチ）の正規表現に「|」を使って繋げて指定してください。
                        # （完全マッチとするためには $ の指定が必要です。）
                        if not re.match(r"RocketDock\.exe$", process_name): # サンプルとして RocketDock.exe を登録

                            # 表示されていないストアアプリ（「設定」等）が window_list に登録されるのを抑制する
                            if class_name == "Windows.UI.Core.CoreWindow":
                                if title in window_dict:
                                    if window_dict[title] in window_list:
                                        window_list.remove(window_dict[title])
                                else:
                                    window_dict[title] = wnd

                            elif class_name == "ApplicationFrameWindow":
                                if title not in window_dict:
                                    window_dict[title] = wnd
                                    window_list.append(wnd)
                            else:
                                window_list.append(wnd)
            return True

        window_dict = {}
        window_list = []
        Window.enum(makeWindowList, None)

        return window_list

    def previous_window():
        self_insert_command("A-S-Tab")()

    def next_window():
        self_insert_command("A-Tab")()

    def move_window_to_previous_display():
        self_insert_command("W-S-Left")()

    def move_window_to_next_display():
        self_insert_command("W-S-Right")()

    def minimize_window():
        wnd = keymap.getTopLevelWindow()
        if wnd and not wnd.isMinimized():
            wnd.minimize()

    def restore_window():
        window_list = getWindowList()

        # ウィンドウのリストアが最小化した順番の逆順にならないときは次の行を無効化
        # （コメント化）してください
        window_list.reverse()

        for wnd in window_list:
            if wnd.isMinimized():
                wnd.restore()
                break

    def previous_desktop():
        self_insert_command("W-C-Left")()

    def next_desktop():
        self_insert_command("W-C-Right")()

    def move_window_to_previous_desktop():
        self_insert_command("W-C-A-Left")()

    def move_window_to_next_desktop():
        self_insert_command("W-C-A-Right")()

    ##################################################
    ## キーバインド（デスクトップ用）
    ##################################################

    # 表示しているウィンドウの中で、一番最近までフォーカスがあったウィンドウに移動
    define_key(keymap_global, other_window_key, reset_search(reset_undo(reset_counter(reset_mark(other_window)))))

    # アクティブウィンドウの切り替え
    for previous_key, next_key in window_switching_key:
        define_key(keymap_global, previous_key, reset_search(reset_undo(reset_counter(reset_mark(previous_window)))))
        define_key(keymap_global, next_key,     reset_search(reset_undo(reset_counter(reset_mark(next_window)))))

    # アクティブウィンドウのディスプレイ間移動
    for previous_key, next_key in window_movement_key_for_displays:
        define_key(keymap_global, previous_key, move_window_to_previous_display)
        define_key(keymap_global, next_key,     move_window_to_next_display)

    # ウィンドウの最小化、リストア
    for restore_key, minimize_key in window_minimize_key:
        define_key(keymap_global, restore_key,  reset_search(reset_undo(reset_counter(reset_mark(restore_window)))))
        define_key(keymap_global, minimize_key, reset_search(reset_undo(reset_counter(reset_mark(minimize_window)))))

    # 仮想デスクトップの切り替え
    for previous_key, next_key in desktop_switching_key:
        define_key(keymap_global, previous_key, reset_search(reset_undo(reset_counter(reset_mark(previous_desktop)))))
        define_key(keymap_global, next_key,     reset_search(reset_undo(reset_counter(reset_mark(next_desktop)))))

    # アクティブウィンドウ仮想デスクトップの切り替え
    for previous_key, next_key in window_movement_key_for_desktops:
        define_key(keymap_global, previous_key, move_window_to_previous_desktop)
        define_key(keymap_global, next_key,     move_window_to_next_desktop)

    # IME の「単語登録」プログラムの起動
    define_key(keymap_global, word_register_key, keymap.ShellExecuteCommand(None, word_register_name, word_register_param, ""))


    ####################################################################################################
    ## タスク切り替え画面の設定
    ####################################################################################################

    def is_task_switching_window(window):
        if window.getClassName() in ("MultitaskingViewFrame", "TaskSwitcherWnd"):
            return True
        return False

    keymap_tsw = keymap.defineWindowKeymap(check_func=is_task_switching_window)

    ##################################################
    ## キーバインド（タスク切り替え画面用）
    ##################################################

    define_key(keymap_tsw, "A-b", previous_window)
    define_key(keymap_tsw, "A-f", next_window)
    define_key(keymap_tsw, "A-p", previous_window)
    define_key(keymap_tsw, "A-n", next_window)
    define_key(keymap_tsw, "A-g", self_insert_command("A-Esc"))


    ####################################################################################################
    ## リストウィンドウの設定
    ####################################################################################################

    # リストウィンドウはクリップボードリストで利用していますが、クリップボードリストの機能を
    # Emacsキーバインドを適用していないアプリケーションソフトでも利用できるようにするため、
    # クリップボードリストで Enter を押下した際の挙動を、次のとおりに切り分けています。
    #
    # １）Emacsキーバインドを適用しているアプリケーションソフトからクリップボードリストを起動
    # 　　→   Enter（テキストの貼り付け）
    # ２）Emacsキーバインドを適用していないアプリケーションソフトからクリップボードリストを起動
    # 　　→ S-Enter（テキストをクリップボードに格納）
    #
    # （Emacsキーバインドを適用しないアプリケーションソフトには、キーの入出力の方式が特殊な
    # 　ものが多く指定されているため、テキストの貼り付けがうまく機能しないものがあります。
    # 　このため、アプリケーションソフトにペーストする場合は、そのアプリケーションソフトの
    # 　ペースト操作で行うことを前提とし、上記のとおりの仕様としてます。もし、どうしても
    # 　Enter（テキストの貼り付け）の入力を行いたい場合には、C-m の押下により対応できます。
    # 　なお、C-Enter（引用記号付で貼り付け）の置き換えは、対応が複雑となるため行っておりません。）

    keymap.setFont("ＭＳ ゴシック", 12)

    def is_list_window(window):
        if window.getClassName() == "KeyhacWindowClass" and window.getText() != "Keyhac":
            return True
        return False

    keymap_lw = keymap.defineWindowKeymap(check_func=is_list_window)

    # リストウィンドウで検索が開始されると True になる
    fakeymacs.lw_is_searching = False

    ##################################################
    ## 文字列検索 / 置換（リストウィンドウ用）
    ##################################################

    def lw_isearch(direction):
        if fakeymacs.lw_is_searching:
            self_insert_command({"backward":"Up", "forward":"Down"}[direction])()
        else:
            self_insert_command("f")()
            fakeymacs.lw_is_searching = True

    def lw_isearch_backward():
        lw_isearch("backward")

    def lw_isearch_forward():
        lw_isearch("forward")

    ##################################################
    ## その他（リストウィンドウ用）
    ##################################################

    def lw_keyboard_quit():
        self_insert_command("Esc")()

    ##################################################
    ## 共通関数（リストウィンドウ用）
    ##################################################

    def lw_newline():
        if fakeymacs.keybind == "emacs":
            self_insert_command("Enter")()
        else:
            self_insert_command("S-Enter")()

    def lw_exit_search(func):
        def _func():
            if fakeymacs.lw_is_searching:
                self_insert_command("Enter")()
            func()
        return _func

    def lw_reset_search(func):
        def _func():
            func()
            fakeymacs.lw_is_searching = False
        return _func

    ##################################################
    ## キーバインド（リストウィンドウ用）
    ##################################################

    ## Escキーの設定
    define_key(keymap_lw, "Esc",           lw_reset_search(self_insert_command("Esc")))
    define_key(keymap_lw, "C-OpenBracket", lw_reset_search(self_insert_command("Esc")))

    ## 「カーソル移動」のキー設定
    define_key(keymap_lw, "C-b", backward_char)
    define_key(keymap_lw, "A-b", backward_char)

    define_key(keymap_lw, "C-f", forward_char)
    define_key(keymap_lw, "A-f", forward_char)

    define_key(keymap_lw, "C-p", previous_line)
    define_key(keymap_lw, "A-p", previous_line)

    define_key(keymap_lw, "C-n", next_line)
    define_key(keymap_lw, "A-n", next_line)

    if scroll_key:
        if scroll_key[0]:
            define_key(keymap_lw, scroll_key[0].replace("M-", "A-"), scroll_up)
        if scroll_key[1]:
            define_key(keymap_lw, scroll_key[1].replace("M-", "A-"), scroll_down)
        if scroll_key[2]:
            define_key(keymap_lw, scroll_key[2].replace("M-", "A-"), scroll_down)

    ## 「カット / コピー / 削除 / アンドゥ」のキー設定
    define_key(keymap_lw, "C-h", delete_backward_char)
    define_key(keymap_lw, "A-h", delete_backward_char)

    define_key(keymap_lw, "C-d", delete_char)
    define_key(keymap_lw, "A-d", delete_char)

    ## 「文字列検索 / 置換」のキー設定
    define_key(keymap_lw, "C-r", lw_isearch_backward)
    define_key(keymap_lw, "A-r", lw_isearch_backward)

    define_key(keymap_lw, "C-s", lw_isearch_forward)
    define_key(keymap_lw, "A-s", lw_isearch_forward)

    ## 「その他」のキー設定
    define_key(keymap_lw, "Enter", lw_exit_search(lw_newline))
    define_key(keymap_lw, "C-m",   lw_exit_search(lw_newline))
    define_key(keymap_lw, "A-m",   lw_exit_search(lw_newline))

    define_key(keymap_lw, "C-g", lw_reset_search(lw_keyboard_quit))
    define_key(keymap_lw, "A-g", lw_reset_search(lw_keyboard_quit))

    define_key(keymap_lw, "S-Enter", lw_exit_search(self_insert_command("S-Enter")))
    define_key(keymap_lw, "C-Enter", lw_exit_search(self_insert_command("C-Enter")))
    define_key(keymap_lw, "A-Enter", lw_exit_search(self_insert_command("C-Enter")))


    ####################################################################################################
    ## クリップボードリストの設定
    ####################################################################################################
    if 1:
        # クリップボードリストを利用するための設定です。クリップボードリストは clipboardList_key 変数で
        # 設定したキーの押下により起動します。クリップボードリストを開いた後、C-f（→）や C-b（←）
        # キーを入力することで画面を切り替えることができます。
        # （参考：https://github.com/crftwr/keyhac/blob/master/_config.py）

        # リストウィンドウのフォーマッタを定義する
        list_formatter = "{:30}"

        # 定型文
        fixed_items = [
            ["---------+ x 8", "---------+" * 8],
            ["メールアドレス", "user_name@domain_name"],
            ["住所",           "〒999-9999 ＮＮＮＮＮＮＮＮＮＮ"],
            ["電話番号",       "99-999-9999"],
        ]
        fixed_items[0][0] = list_formatter.format(fixed_items[0][0])

        import datetime

        # 日時をペーストする機能
        def dateAndTime(fmt):
            def _func():
                return datetime.datetime.now().strftime(fmt)
            return _func

        # 日時
        datetime_items = [
            ["YYYY/MM/DD HH:MM:SS", dateAndTime("%Y/%m/%d %H:%M:%S")],
            ["YYYY/MM/DD",          dateAndTime("%Y/%m/%d")],
            ["HH:MM:SS",            dateAndTime("%H:%M:%S")],
            ["YYYYMMDD_HHMMSS",     dateAndTime("%Y%m%d_%H%M%S")],
            ["YYYYMMDD",            dateAndTime("%Y%m%d")],
            ["HHMMSS",              dateAndTime("%H%M%S")],
        ]
        datetime_items[0][0] = list_formatter.format(datetime_items[0][0])

        keymap.cblisters += [
            ["定型文",  cblister_FixedPhrase(fixed_items)],
            ["日時",    cblister_FixedPhrase(datetime_items)],
        ]

        def lw_clipboardList():
            keymap.command_ClipboardList()

        # クリップボードリストを起動する
        define_key(keymap_global, clipboardList_key, lw_reset_search(reset_search(reset_undo(reset_counter(reset_mark(lw_clipboardList))))))


    ####################################################################################################
    ## ランチャーリストの設定
    ####################################################################################################
    if 1:
        # ランチャー用のリストを利用するための設定です。ランチャーリストは lancherList_key 変数で
        # 設定したキーの押下により起動します。ランチャーリストを開いた後、C-f（→）や C-b（←）
        # キーを入力することで画面を切り替えることができます。
        # （参考：https://github.com/crftwr/keyhac/blob/master/_config.py）

        def lw_lancherList():
            def popLancherList():

                # リストウィンドウのフォーマッタを定義する
                list_formatter = "{:30}"

                # 既にリストが開いていたら閉じるだけ
                if keymap.isListWindowOpened():
                    keymap.cancelListWindow()
                    return

                # ウィンドウ
                window_list = getWindowList()
                window_items = []
                if window_list:
                    processName_length = max(map(len, map(Window.getProcessName, window_list)))

                    formatter = "{0:" + str(processName_length) + "} | {1}"
                    for wnd in window_list:
                        window_items.append((formatter.format(wnd.getProcessName(), wnd.getText()), popWindow(wnd)))

                window_items.append((list_formatter.format("<Desktop>"), keymap.ShellExecuteCommand(None, r"shell:::{3080F90D-D7AD-11D9-BD98-0000947B0257}", "", "")))

                # アプリケーションソフト
                application_items = [
                    ["Notepad",     keymap.ShellExecuteCommand(None, r"notepad.exe", "", "")],
                    ["Explorer",    keymap.ShellExecuteCommand(None, r"explorer.exe", "", "")],
                    ["Cmd",         keymap.ShellExecuteCommand(None, r"cmd.exe", "", "")],
                    ["MSEdge",      keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "", "")],
                    ["Chrome",      keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "", "")],
                    ["Firefox",     keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe", "", "")],
                    ["Thunderbird", keymap.ShellExecuteCommand(None, r"C:\Program Files (x86)\Mozilla Thunderbird\thunderbird.exe", "", "")],
                ]
                application_items[0][0] = list_formatter.format(application_items[0][0])

                # ウェブサイト
                website_items = [
                    ["Google",          keymap.ShellExecuteCommand(None, r"https://www.google.co.jp/", "", "")],
                    ["Facebook",        keymap.ShellExecuteCommand(None, r"https://www.facebook.com/", "", "")],
                    ["Twitter",         keymap.ShellExecuteCommand(None, r"https://twitter.com/", "", "")],
                    ["Keyhac",          keymap.ShellExecuteCommand(None, r"https://sites.google.com/site/craftware/keyhac-ja", "", "")],
                    ["Fakeymacs",       keymap.ShellExecuteCommand(None, r"https://github.com/smzht/fakeymacs", "", "")],
                    ["NTEmacs＠ウィキ", keymap.ShellExecuteCommand(None, r"http://w.atwiki.jp/ntemacs/", "", "")],
                ]
                website_items[0][0] = list_formatter.format(website_items[0][0])

                # その他
                other_items = [
                    ["Edit   config.py", keymap.command_EditConfig],
                    ["Reload config.py", keymap.command_ReloadConfig],
                ]
                other_items[0][0] = list_formatter.format(other_items[0][0])

                listers = [
                    ["Window",  cblister_FixedPhrase(window_items)],
                    ["App",     cblister_FixedPhrase(application_items)],
                    ["Website", cblister_FixedPhrase(website_items)],
                    ["Other",   cblister_FixedPhrase(other_items)],
                ]

                try:
                    select_item = keymap.popListWindow(listers)

                    if not select_item:
                        Window.find("Progman", None).setForeground()
                        select_item = keymap.popListWindow(listers)

                    if select_item and select_item[0] and select_item[0][1]:
                        select_item[0][1]()
                except:
                    print("エラーが発生しました")

            # キーフックの中で時間のかかる処理を実行できないので、delayedCall() を使って遅延実行する
            keymap.delayedCall(popLancherList, 0)

        # ランチャーリストを起動する
        define_key(keymap_global, lancherList_key, lw_reset_search(reset_search(reset_undo(reset_counter(reset_mark(lw_lancherList))))))


    ####################################################################################################
    ## C-Enter に F2（編集モード移行）を割り当てる（オプション）
    ####################################################################################################
    if 0:
        edit_mode_target = [["EXCEL.EXE",    "EXCEL*"],
                            ["explorer.exe", "DirectUIHWND"]]

        def is_edit_mode_target(window):
            for processName, className in edit_mode_target:
                if checkWindow(processName, className, window):
                    return True
            return False

        keymap_edit_mode = keymap.defineWindowKeymap(check_func=is_edit_mode_target)

        define_key(keymap_edit_mode, "C-Enter", reset_search(reset_undo(reset_counter(reset_mark(self_insert_command("F2"))))))


    ####################################################################################################
    ## Emacs の場合、IME 切り替え用のキーを C-\ に置き換える（オプション）
    ####################################################################################################
    if 0:
        # Emacs で mozc を利用する際に Windows の IME の切換えキーを mozc の切り替えキーとして
        # 機能させるための設定です。初期設定では NTEmacs（gnupack 含む）と Windows の Xサーバで動く
        # Emacs を指定しています。

        def is_real_emacs(window):
            if (window.getClassName() == "Emacs" or
                (window.getProcessName() in ["XWin.exe",          # Cygwin/X
                                             "XWin_MobaX.exe",    # MobaXterm/X
                                             "Xming.exe",         # Xming
                                             "vcxsrv.exe",        # VcXsrv
                                             "Xpra-Launcher.exe"] # Xpra
                 and
                 # ウィンドウのタイトルを検索する正規表現を指定する
                 # Emacs を起動しているウィンドウを検索できるように、Emacs の frame-title-format 変数を
                 # 次のように設定するなどして、識別できるようにする
                 # (setq frame-title-format (format "emacs-%s - %%b" emacs-version))
                 re.search(r"^emacs-", window.getText()))):
                return True
            return False

        keymap_real_emacs = keymap.defineWindowKeymap(check_func=is_real_emacs)

        # IME 切り替え用のキーの置き換え
        # （Emacs 側での C-F1 と C-F2 の設定については、次のページを参照してください。
        #   https://w.atwiki.jp/ntemacs/pages/48.html ）
        keymap_real_emacs["(243)"]  = keymap.InputKeyCommand("C-Yen") # [半角／全角] キー
        keymap_real_emacs["(244)"]  = keymap.InputKeyCommand("C-Yen") # [半角／全角] キー
        keymap_real_emacs["A-(25)"] = keymap.InputKeyCommand("C-Yen") # Alt-` キー

        keymap_real_emacs["(29)"]   = keymap.InputKeyCommand("C-F1")  # [無変換] キー
        keymap_real_emacs["(28)"]   = keymap.InputKeyCommand("C-F2")  # [変換] キー
        # keymap_real_emacs["O-LAlt"] = keymap.InputKeyCommand("C-F1")  # 左 Alt キーのワンショットモディファイア
        # keymap_real_emacs["O-RAlt"] = keymap.InputKeyCommand("C-F2")  # 右 Alt キーのワンショットモディファイア


    ####################################################################################################
    ## 英語キーボード設定をした OS 上で、日本語キーボードを混在して利用する場合の切り替えを行う（オプション）
    ####################################################################################################
    if 0:
        # https://w.atwiki.jp/ntemacs/pages/90.html

        def change_keyboard():
            if fakeymacs.keyboard_status == "US":
                # 日本語キーボードの利用に切り替える

                # 日本語キーボードの [ ]] キーを Enter キーにする
                keymap.replaceKey("BackSlash", "Return")

                # 初代 HHKB を利用している場合は、次の if 文を有効にする
                if 0:
                    keymap.replaceKey("LAlt", "LAlt")
                    keymap.replaceKey("RAlt", "RAlt")
                    keymap.replaceKey(235, 29)
                    keymap.replaceKey(255, 28)

                keymap.popBalloon("keyboard", "[JP Keyboard]", 1000)
                fakeymacs.keyboard_status = "JP"

            else:
                # 英語キーボードの利用に切り替える

                # 日本語キーボードの [ ]] キーを元の設定に戻す
                keymap.replaceKey("BackSlash", "BackSlash")

                # 初代 HHKB を利用している場合は、次の if 文を有効にする
                if 0:
                    keymap.replaceKey("LAlt", "LWin")
                    keymap.replaceKey("RAlt", "RCtrl")
                    keymap.replaceKey(235, "LAlt")
                    keymap.replaceKey(255, "RAlt")

                if fakeymacs.keyboard_status == "JP":
                    keymap.popBalloon("keyboard", "[US Keyboard]", 1000)
                fakeymacs.keyboard_status = "US"

        fakeymacs.keyboard_status = None
        change_keyboard()

        define_key(keymap_global, "C-S-c", change_keyboard)
