 {
   packageOverrides = pkgs : with pkgs; {
     sdlEnv = pkgs.myEnvFun {
         name = "alt_trezor_lib";
         buildInputs = [ stdenv SDL SDL_image SDL_ttf SDL_gfx cmake SDL_net pkgconfig ];
     };
   };
 }