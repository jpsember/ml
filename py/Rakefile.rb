
rule '.pdf' => '.dot' do |t|
  system("dot -o#{t.name} -Tpdf #{t.source}")
end

desc "Compile dot files to pdf"
task :dotfiles => FileList.new("**/*.dot").map{|x| x.chomp("dot") + "pdf"}

desc "Run program, recompile dot files"
task :default do
  system("backprop.py")
  Rake::Task["dotfiles"].invoke
end
