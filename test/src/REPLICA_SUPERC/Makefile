EXE=ed_replica_superc
FC=mpif90
PLAT=gnu
TSTBIN=../../bin/REPLICA/SUPERC
OBJS=../ASSERTING.o ../COMMON.o

#NO NEED TO CHANGE DOWN HERE, only expert mode.
#########################################################################
GLOB_INC:=$(shell pkg-config --cflags edipack scifor)
GLOB_LIB:=$(shell pkg-config --libs   edipack scifor | sed  "s/;/ /g"  | sed 's/\\/  /g')


ifeq ($(PLAT),intel)
FFLAG=-O2 -ftz
OFLAG=-O3 -ftz
DFLAG=-p -O0 -g -fpe0 -warn -warn errors -debug extended -traceback -check all,noarg_temp_created
FPPFLAG =-fpp
endif
ifeq ($(PLAT),gnu)
FFLAG = -O2 -ffree-line-length-none 
DFLAG = -O2 -p -g -fimplicit-none -Wsurprising  -Waliasing -fwhole-file -fcheck=all -pedantic -fbacktrace -ffree-line-length-none
OFLAG = -O3 -ffast-math -march=native -funroll-loops -ffree-line-length-none
FPPFLAG =-cpp -D_MPI
endif


##$ Extends the implicit support of the Makefile to .f90 files
.SUFFIXES: .f90 .o

all: FLAG:=${FFLAG} ${FPPFLAG}
all: $(OBJS)
	$(FC) $(FLAG) $(OBJS) $(EXE).f90 -o $(TSTBIN)/$(EXE).x -I../ ${GLOB_INC} ${GLOB_LIB}
	@cp *.check *.in *.restart $(TSTBIN)/

debug: FLAG:=${DFLAG} ${FPPFLAG}
debug: $(OBJS)
	$(FC) $(FLAG) $(OBJS) $(EXE).f90 -o $(TSTBIN)/$(EXE).x -I../ ${GLOB_INC} ${GLOB_LIB}
	@cp *.check *.in *.restart $(TSTBIN)/

.f90.o:
	$(FC) $(FFLAGS) -c $< ${GLOB_INC} -J../ -o$@

clean: 
	@echo "Cleaning bath:REPLICA mode:SUPERC"
	@rm -rf *.mod *.o *~
	@rm -fv  $(TSTBIN)/$(EXE)



#########################################################################
