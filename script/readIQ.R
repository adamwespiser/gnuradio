f = "rtl2832u_fm_sample_FIXED_double_cols_Mil.space"
df <- read.csv(file=f, stringsAsFactors=FALSE, header=FALSE,sep=" ")



df$r = (df$V1 - 127) * 0.008
df$i = (df$V2 - 127) * 0.008

df$complex = complex(real=df$r,imaginary=df$i)


df$mag = sqrt(df$r * df$r + df$i * df$i) 

df$fft = fft(df$complex)


n = 2400000L
readBin(signed = FALSE,size=1L,  con = file("~/Downloads/rtl2832u_fm_sample_FIXED.bin","rb"),what="int",n=n*9L,endian="big") -> chr;

one <- chr[seq_along(chr) %% 2 == 0]
two <- chr[seq_along(chr) %% 2 == 1]

one.dec <- (one - 127) * 0.008
two.dec <- (two - 127) * 0.008
comp = complex(real=one.dec, imaginary=two.dec)

mag = sqrt(one.dec^2 + two.dec ^2)
phi = atan2(y=two.dec,x=one.dec) 
phidiff = atan2(y=two.dec,x=one.dec)


plotIQ <- function(start,len){
		if (missing(start)){
				start = length(one.dec)/2 
		}
		if (missing(len)){
				len = 10000
		}
		pr = seq(from=start,to=start+len,by=1)

		plot(one.dec[pr], type="l", col="blue")
		lines(two.dec[pr], col="red")
}

relD <- function(x,y) 2* abs(x - y) / abs(x + y)
magIm <- function(img){sqrt(Re(img)^2 + Im(img)^2)}

# sampling rate is ~ 40hz
cos(1:10000/(2*pi))
# fft is being taken on 1024 points
trans = fft(cos(1:10000/(2*pi))[1:1024])
# get the index of the max fft transform
maxIndex = which(magIm(trans) == max(magIm(trans)))[1]
# frequency at fft bin n = (bin n) * ((sampling rate)/(number of samples)
freq = maxIndex * (40/1024)













