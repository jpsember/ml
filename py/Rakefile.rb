CIFAR_SUBSET_PATH = "assets/cifar_subset.bin"

rule '.pdf' => '.dot' do |t|
  system("dot -o#{t.name} -Tpdf #{t.source}")
end

desc "Compile dot files to pdf"
task :dotfiles => FileList.new("**/*.dot").map{|x| x.chomp("dot") + "pdf"}

desc "Run program, recompile dot files"
task :default => [CIFAR_SUBSET_PATH] do
  system("backprop.py")
  Rake::Task["dotfiles"].invoke
end

desc "Generate cropped subset of cifar images"
file CIFAR_SUBSET_PATH do
  system("cifar.py")
end
