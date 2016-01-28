      program refl3d
c
c---- Reflects the partial 3d grid for C2 c9h9+ as
c---- (x,y,z) -> (-x,-y,z)
c---- and prints GAUSSIAN cube data in x, y, z order
c---- (z changes fastest, followed by y and x)
c
      implicit real*8 (a-h, o-z)
      character*50 inputFileName, outputFileName
      parameter (nx = 70, ny = 90, nz = 70, delta = 0.05d0)
      parameter (br = 0.5291772083d0)
      dimension w(-nx:nx,-ny:ny,-nz:nz,2)
      inputFileName = "c2f"
      outputFileName = "cubef"
c
      do 10 ix = 0, nx
      do 10 iy = 0, ny
      do 10 iz = 0, nz
        read (5, *) siso, sani
c------ (x,y,z)
c        w(ix, iy, iz, 1) = siso
c        w(ix, iy, iz, 2) = sani
c------ (-x,y,z)
c        w(-ix, iy, iz, 1) = siso
c        w(-ix, iy, iz, 2) = sani
c------ (-x,-y,z)
c        w(-ix, -iy, iz, 1) = siso
c        w(-ix, -iy, iz, 2) = sani
c------ (x,-y,z)
        w(ix, -iy, iz, 1) = siso
        w(ix, -iy, iz, 2) = sani
c------ (x,y,-z)
c        w(ix, iy, -iz, 1) = siso
c        w(ix, iy, -iz, 2) = sani
c------ (-x,y,-z)
c        w(-ix, iy, -iz, 1) = siso
c        w(-ix, iy, -iz, 2) = sani
c------ (-x,-y,-z)
c        w(-ix, -iy, -iz, 1) = siso
c        w(-ix, -iy, -iz, 2) = sani
c------ (x,-y,-z)
c        w(ix, -iy, -iz, 1) = siso
c        w(ix, -iy, -iz, 2) = sani
   10 continue
c
      write (6, *) 'C9H9+ C2 S=0 HF/6-311++G(d,p) iso shielding'
      write (6, *) 'x,y,z: -3.5(0.05)3.5 A exp. geom. (1.3964/1.0831)'
      write (6, '(i7, 3F16.6)')
     .  12, -nx*delta/br, -ny*delta/br, -nz*delta/br
      write (6, '(i7, 3F16.6)') 2*nx + 1, delta/br, 0d0, 0d0
      write (6, '(i7, 3F16.6)') 2*ny + 1, 0d0, delta/br, 0d0
      write (6, '(i7, 3F16.6)') 2*nz + 1, 0d0, 0d0, delta/br
      write (6, 1000) 6, 6d0,   0.0,             1.3964/br,  0d0
      write (6, 1000) 6, 6d0,   1.209317874/br,  0.6982/br,  0d0
      write (6, 1000) 6, 6d0,   1.209317874/br, -0.6982/br,  0d0
      write (6, 1000) 6, 6d0,   0.0,            -1.3964/br,  0d0
      write (6, 1000) 6, 6d0,  -1.209317874/br, -0.6982/br,  0d0
      write (6, 1000) 6, 6d0,  -1.209317874/br,  0.6982/br,  0d0
      write (6, 1000) 1, 1d0,   0.0,             2.4795/br,  0d0
      write (6, 1000) 1, 1d0,   2.147309989/br,  1.23975/br, 0d0
      write (6, 1000) 1, 1d0,   2.147309989/br, -1.23975/br, 0d0
      write (6, 1000) 1, 1d0,   0.0,            -2.4795/br,  0d0
      write (6, 1000) 1, 1d0,  -2.147309989/br, -1.23975/br, 0d0
      write (6, 1000) 1, 1d0,  -2.147309989/br,  1.23975/br, 0d0
      do 20 ix = -nx, nx
      do 20 iy = -ny, ny
        write(6,'(6E13.5)') (w(ix, iy, iz, 1), iz = -nz, nz)
   20 continue
c
 1000 format (i7, 4F16.6)
      end
