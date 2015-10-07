
with import <nixpkgs> {};

with pkgs.python27Packages;


buildPythonPackage { name = "impurePythonEnv"
                   
                   ; buildInputs = [  git
                                      libxml2
                                      libxslt
                                      libzip
                                      python27Full
                                      python27Packages.virtualenv
                                      pyqt4
                                      stdenv
                                      glibc
                                      zlib 
                                      wine
                                   ]
                   ; src = null
                   
                   ; # When used as `nix-shell --pure`
                     shellHook = ''
                                    unset http_proxy
                                    export GIT_SSL_CAINFO=/etc/ssl/certs/ca-bundle.crt
                                 ''
                   ; # used when building environments
                     extraCmds = ''
                                    unset http_proxy # otherwise downloads will fail ("nodtd.invalid")
                                    export GIT_SSL_CAINFO=/etc/ssl/certs/ca-bundle.crt
                                 ''
                  ;}
