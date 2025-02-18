{  
  inputs = {  
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";  
    flake-utils.url = "github:numtide/flake-utils";  
  };  

  outputs = { self, nixpkgs, flake-utils }:  
    flake-utils.lib.eachDefaultSystem (system:  
      let  
        pkgs = nixpkgs.legacyPackages.${system};  
      in {  
        devShells.default = pkgs.mkShell {  
          packages = with pkgs; [  
            python3  
            uv  
          ];  

          shellHook = ''  
            [ ! -d .venv ] && uv venv  
            source .venv/bin/activate  
            uv pip install -e .  
          '';  
        };  
      });  
}  
